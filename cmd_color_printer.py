class ColorPrinter:
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m",
    }

    def __init__(self) -> None:
        print()

    def colored_print(text: str, color: str) -> None:
        if color in ColorPrinter.colors:
            print(f"{ColorPrinter.colors[color]}{text}{ColorPrinter.colors['reset']}")
        else:
            print(text)
