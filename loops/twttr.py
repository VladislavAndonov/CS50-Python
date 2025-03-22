def main():
    user_input = input("Input: ").strip()

    print(shorten(user_input))


def shorten(text):
    shorten_word = ""

    for l in text:
        if l.lower() != "a" and l.lower() != "e" and l.lower() != "i" and l.lower() != "o" and l.lower() != "u":
            shorten_word += l

    return shorten_word


if __name__ == "__main__"():
    main()
