import ctypes
import random

def trigger_buffer_overflow(user_input):
    input = user_input['input']
    if not input.isdigit():
        return "invalid input"
    d_input = int(input)
    buffer = (ctypes.c_char * d_input)()
    
    for i in range(d_input):
        buffer[i] = b'A' 
    try:
        buffer[d_input + random.randint(-5, 2)] = b'B'
    except IndexError as e:
        return ("overflow:", e)
    return ("buffer:", bytes(buffer))