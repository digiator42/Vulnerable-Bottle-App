import ctypes
from config.settings import DEFAULT_LEVEL
from bottle import request


MAX_LEN = 15

def trigger_buffer_overflow(user_input):
    input = user_input['input']
    session = request.environ.get('beaker.session')
    level = session['level']
    
    if level == DEFAULT_LEVEL:
        return weak_buffer_overflow(input)

def weak_buffer_overflow(input):
    buffer = (ctypes.c_char * MAX_LEN)()
    
    try:
        for i in range(len(input)):
            buffer[i] = input[i].encode('utf-8')
    except TypeError as e:
        return e
    except IndexError:
        return 'Buffer overflow at index: ' + str(i)
    
    return 'Hello ' + buffer.value.decode('utf-8', 'ignore')