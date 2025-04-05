def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)

        if isinstance(percentage, int):
            print(gauge(percentage))
            break


def convert(fraction):
    try:
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError

    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return ZeroDivisionError

    return round(x / y * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
