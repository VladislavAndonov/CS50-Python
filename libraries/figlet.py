from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()


def main():

    if len(sys.argv) == 1:
        figlet.setFont(font=(random.choice(fonts)))
    elif len(sys.argv) > 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")
    else:
        if sys.argv[1] != "--font" and sys.argv[1] != "-f":
            sys.exit("Invalid usage")

        if not sys.argv[2] in fonts:
            sys.exit("Invalid usage")

        figlet.setFont(font=sys.argv[2])

    text = get_text()

    print(f"Output: {text}")


def get_text():
    text = input("Input: ").strip()
    return figlet.renderText(text)


main()
