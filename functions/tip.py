def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    format_d = d.replace("$", '')
    conver_d = float(format_d)
    return conver_d

def percent_to_float(p):
    format_p = p.replace("%", '')
    convert_d = float(format_p)
    result = convert_d / 100
    return result

main()
