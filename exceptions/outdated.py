months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():

    get_date()


def get_date():
    while True:
        date = input("Date: ").strip()

        try:
            [month, day, year] = date.split("/")
        except ValueError:
            try:
                [month_and_day, year] = date.split(", ")
                [month, day] = month_and_day.split(" ")
            except ValueError:
                pass
            else:
                if not month in months:
                    continue
                else:
                    month = months.index(month) + 1

                day = int(day)

                if day < 1 or day > 31:
                    continue

                return print(f"{year}-{month:02}-{day:02}")
        else:
            if not month.isdigit():
                continue
            else:
                month = int(month)

            day = int(day)

            if day < 1 or day > 31:
                continue
            if month < 1 or month > 12:
                continue

            return print(f"{year}-{month:02}-{day:02}")


main()
