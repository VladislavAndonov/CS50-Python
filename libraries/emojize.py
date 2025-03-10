import emoji


def main():
    result = get_emoji()
    print(f"Output {result}")


def get_emoji():
    str = input("Input: ").strip()
    return emoji.emojize(str, language='alias')


main()
