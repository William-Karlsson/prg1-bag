import ctypes

kernel32 = ctypes.windll.kernel32
stdin_handle = kernel32.GetStdHandle(-10)  # STD_INPUT_HANDLE

MOUSE_MODE = 0x0001 | 0x0010 | 0x0080
NORMAL_MODE = 0x0001 | 0x0002 | 0x0004 | 0x0040 | 0x0080

def enable_fancy_input():
    kernel32.FlushConsoleInputBuffer(stdin_handle)
    kernel32.SetConsoleMode(stdin_handle, MOUSE_MODE)

def enable_normal_input():
    kernel32.FlushConsoleInputBuffer(stdin_handle)
    kernel32.SetConsoleMode(stdin_handle, NORMAL_MODE)

event_buffer = ctypes.create_string_buffer(32)
events_read = ctypes.c_ulong(0)
num_events = ctypes.c_ulong(0)

def check_console_input():
    while True:
        kernel32.GetNumberOfConsoleInputEvents(stdin_handle, ctypes.byref(num_events))
        
        if num_events.value == 0:
            return None, None

        if kernel32.ReadConsoleInputA(stdin_handle, event_buffer, 1, ctypes.byref(events_read)):
            event_type = int.from_bytes(event_buffer[0:2], byteorder='little')

            # (Tangentbord)
            if event_type == 0x0001:
                key_down = int.from_bytes(event_buffer[4:8], byteorder='little')
                if key_down:
                    ascii_char = event_buffer[14:15].decode('ascii', errors='ignore')
                    if ascii_char:
                        return "key", ascii_char.lower()

            # (Mus)
            elif event_type == 0x0002:
                event_flags = int.from_bytes(event_buffer[16:20], byteorder='little')
                
                if event_flags in (0, 2):
                    x = int.from_bytes(event_buffer[4:6], byteorder='little', signed=True) + 1
                    y = int.from_bytes(event_buffer[6:8], byteorder='little', signed=True) + 1
                    button_state = int.from_bytes(event_buffer[8:12], byteorder='little')
                    return "mouse", (x, y, button_state)
