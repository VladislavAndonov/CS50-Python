menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    get_item()


def get_item():
    global menu
    price = 0

    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            return print()
        else:
            if item:
                if item in menu:
                    price += menu[item]
                    print(f"Total: ${price:.2f}")
                else:
                    continue
            else:
                break


main()
