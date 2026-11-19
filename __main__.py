import msvcrt
from core.bag import Bag
from core.visuals.clear_screen import clear_screen
from core.visuals.color import colors
from core.input_handler import check_console_input, enable_fancy_input

bag = Bag()

def get_key_non_blocking():
    if msvcrt.kbhit():
        return msvcrt.getwch()  
    return ""

def show_instructions():
    print(f"Välkommen till {colors.GREEN}Påsen{colors.ENDC}! Vänligen ange ett {colors.CYAN}kommando{colors.ENDC}, du kan alternativt {colors.CYAN}klicka{colors.ENDC} på ett kommando i menyn: \n"
    f"   ({colors.PURPLE}v{colors.ENDC}) Visa påse \n"
    f"   ({colors.PURPLE}a{colors.ENDC}) Lägg till objekt \n"
    f"   ({colors.PURPLE}r{colors.ENDC}) Ta bort objekt \n"
    f"   ({colors.PURPLE}f{colors.ENDC}) Leta efter objekt \n"
    f"   ({colors.PURPLE}s{colors.ENDC}) Sortera påse \n"
    f"   ({colors.PURPLE}c{colors.ENDC}) Rensa påse \n"
    f"   ({colors.PURPLE}q{colors.ENDC}) Avsluta")

clear_screen()
show_instructions()

enable_fancy_input()

while True:

    event_type, data = check_console_input()

    if event_type == "key":
        if data != "":
            clear_screen()
            show_instructions()

        if data == 'v':
            bag.show_items()
        elif data == 'a':
            bag.add_item()
        elif data == 'r':
            bag.remove_item()
        elif data == 'f':
            bag.find_item()
        elif data == 's':
            bag.sort_items()
        elif data == 'c':
            bag.clear_items()
        elif data == 'q':
            print("Programmet avslutas.")
            break
        elif data != "":
            print(f"{colors.RED}Kommandot är inte giltigt.{colors.ENDC}")

    elif event_type == "mouse":
        x, y, button_state = data

        if button_state & 1:
            clear_screen()
            show_instructions()

            if y == 2:
                bag.show_items()
            elif y == 3:
                bag.add_item()
            elif y == 4:
                bag.remove_item()
            elif y == 5:
                bag.find_item()
            elif y == 6:
                bag.sort_items()
            elif y == 7:
                bag.clear_items()
            elif y == 8:
                print("Programmet avslutas.")
                break
            else:
                print(f"{colors.RED}Du klickade utanför menyn. Vänligen klicka på ett giltigt alternativ.{colors.ENDC}")