import ctypes

def trigger_buffer_overflow():
    buffer = (ctypes.c_char * 10)()
    
    for i in range(10):
        buffer[i] = b'A'    
    try:
        buffer[15] = b'B'
    except IndexError as e:
        print("overflow:", e)
    print("buffer:", bytes(buffer))
