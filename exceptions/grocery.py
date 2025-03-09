items = {}

def main():
    get_item()


def get_item():
    global items

    while True:
        try:
            item = input().strip().upper()

            if item in items:
                items[item] += 1
            else:
                items[item] = 1

        except EOFError:
            print()
            sorted_list = sorted(items)

            for item in sorted_list:
                print(f"{items[item]} {item}")

            return


main()
