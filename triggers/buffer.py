import ctypes
import random

def trigger_buffer_overflow(user_input: int=10):
    if user_input is None or not user_input.isdigit():
        return ("error:", "invalid input")
    user_input = int(user_input)
    buffer = (ctypes.c_char * user_input)()
    
    for i in range(user_input):
        buffer[i] = b'A' 
    try:
        buffer[user_input + random.randint(-5, 2)] = b'B'
    except IndexError as e:
        return ("overflow:", e)
    return ("buffer:", bytes(buffer))