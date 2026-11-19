import ctypes

kernel32 = ctypes.windll.kernel32
stdin_handle = kernel32.GetStdHandle(-10) # STD_INPUT_HANDLE

# Configurera konsollen och slå av att man kan markera text
kernel32.SetConsoleMode(stdin_handle, 0x0010 | 0x0080) 

# För att läsa muspositionen
event_buffer = ctypes.create_string_buffer(32)
events_read = ctypes.c_ulong(0)

try:
    while True:
        if kernel32.ReadConsoleInputA(stdin_handle, event_buffer, 1, ctypes.byref(events_read)): # Vänta på ett event

            event_type = int.from_bytes(event_buffer[0:2], byteorder='little')
            
            if event_type == 0x0002:
                x = int.from_bytes(event_buffer[4:6], byteorder='little', signed=True) + 1
                y = int.from_bytes(event_buffer[6:8], byteorder='little', signed=True) + 1
                button_state = int.from_bytes(event_buffer[8:12], byteorder='little')
                print(f"\033[{y};{x}H{button_state}")
except:
    print("oh noo")