import inflect


def main():
    p = inflect.engine()
    names = get_names()

    if len(names) > 2:
        str_of_names = p.join((names))
    else:
        str_of_names = p.join((names), final_sep="")

    print("Adieu, adieu, to " + str_of_names)


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            return names


main()
