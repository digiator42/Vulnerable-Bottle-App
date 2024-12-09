import ctypes

MAX_LEN = 15

def trigger_buffer_overflow(user_input):
    input = user_input['input']
    
    buffer = (ctypes.c_char * MAX_LEN)()
    
    try:
        for i in range(len(input)):
            buffer[i] = input[i].encode('utf-8')
    except TypeError as e:
        return e
    except IndexError:
        return 'Buffer overflow at index: ' + str(i)
    
    return 'Hello ' + buffer.value.decode('utf-8', 'ignore')