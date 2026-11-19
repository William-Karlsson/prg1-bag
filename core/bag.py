from core.visuals.color import colors
from core.input_handler import enable_normal_input, enable_fancy_input

class Bag:
    def __init__(self):
        self.items = []

    def add_item(self):
        """Lägg till ett objekt i påsen"""
        enable_normal_input()
        item = input("Ange objektet som ska läggas till i påsen: ")
        enable_fancy_input()

        if not item.strip() == "":
            self.items.append(item)
            print(f"{colors.GREEN}{item} har lagts till i påsen.{colors.ENDC}")
        else:
            print(f"{colors.RED}Objektet kan inte vara tomt.{colors.ENDC}")

    def remove_item(self):
        """Ta bort ett objekt från påsen"""
        enable_normal_input()
        item = input("Ange objektet som ska tas bort från påsen: ")
        enable_fancy_input()

        if item in self.items:
            self.items.remove(item)
            print(f"{colors.GREEN}{item} har tagits bort från påsen.{colors.ENDC}")
        else:
            print(f"{colors.RED}{item}{colors.ENDC} finns inte i påsen.")

    def show_items(self):
        """Visa innehållet i påsen"""

        if self.items:
            print(f"{colors.CYAN}Innehållet i påsen:{colors.ENDC}")
            for item in self.items:
                print(f"- {item}")
        else:
            print(f"{colors.CYAN}Påsen är tom.{colors.ENDC}")

    def find_item(self):
        """Leta efter ett objekt i påsen"""
        enable_normal_input()
        item = input("Ange objektet som ska letas efter i påsen: ")
        enable_fancy_input()

        if item in self.items:
            print(f"{colors.GREEN}{item}{colors.ENDC} finns i påsen.")
        else:
            print(f"{colors.RED}{item}{colors.ENDC} finns inte i påsen.")

    def sort_items(self):
        """Sortera påsen"""
        self.items.sort()
        print(f"{colors.GREEN}Påsen har sorterats.{colors.ENDC}")

    def clear_items(self):
        """Rensa påsen"""
        self.items.clear()
        print(f"{colors.GREEN}Påsen har rensats.{colors.ENDC}")