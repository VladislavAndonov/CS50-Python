def main():
    user_input = input("camelCase: ").strip()

    print(convert(user_input))


def convert(camel_case):
    snake_case = ""
    for i in range(len(camel_case)):
        if not camel_case[i].islower():
            snake_case += "_"
            snake_case += camel_case[i].lower()
        else:
            snake_case += (camel_case[i])

    return snake_case


main()
