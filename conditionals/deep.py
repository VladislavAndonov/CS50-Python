def main():

    userInput = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    ).lower()

    answer(userInput)


def answer(userInput):
    match userInput.lower().strip():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()
