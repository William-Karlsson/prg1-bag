def clear_screen() -> None:
    print('\033[2J', end='')
    home()

def home() -> None:
    print('\033[H', end='')