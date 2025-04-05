def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s[0:2].isalpha():
        return False

    if 2 > len(s) or len(s) > 6:
        return False

    for i in range(len(s)):

        if not s[i].isnumeric() and not s[i].isalpha():
            return False

        first_digit_index = -1
        for i, char in enumerate(s):
            if char.isdigit():
                first_digit_index = i
                break

        if first_digit_index != -1:
            if any(char.isalpha() for char in s[first_digit_index:]):
                return False

        if s[first_digit_index] == "0":
            return False

    return True


if __name__ == "__main__":
    main()
