import ctypes
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL
from bottle import request


MAX_LEN = 15

def trigger_buffer_overflow(user_input):
    input = user_input.get('input')
    session = request.environ.get('beaker.session')
    level = session['level']
    
    if level == DEFAULT_LEVEL:
        return weak_buffer_overflow(input)
    elif level == MEDIUM_LEVEL:
        return medium_buffer_overflow(user_input)

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

def medium_buffer_overflow(input):
    first_name = input.get('input')
    second_name = input.get('second_name')
    first_buffer = (ctypes.c_char * MAX_LEN)()
    second_buffer = (ctypes.c_char * MAX_LEN)()
    
    try:
        for i in range(len(first_name)):
            first_buffer[i] = first_name[i].encode('utf-8')
        message = 'Hello ' + first_buffer.value.decode('utf-8', 'ignore') + ' ' + second_buffer.value.decode('utf-8', 'ignore')
    except TypeError as e:
        return e
    except IndexError:
        message = 'Hello ' + first_name[MAX_LEN:] + ' ' + second_name[:MAX_LEN]
        return message
    try:
        for i in range(len(second_name)):
            second_buffer[i] = second_name[i].encode('utf-8')
        message = 'Hello ' + first_buffer.value.decode('utf-8', 'ignore') + ' ' + second_buffer.value.decode('utf-8', 'ignore')
    except TypeError as e:
        return e
    except IndexError:
        message = 'Hello ' + first_name[:MAX_LEN] + ' ' + second_name[MAX_LEN:]
        return message
    
    return message