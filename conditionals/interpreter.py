def main():
    expression = input("Expression: ").strip()

    [x, operator, y] = expression.split(" ")

    x = int(x)
    y = int(y)
    result = 0

    match operator:
        case "+":
            result = x + y
        case "-":
            result = x - y
        case "*":
            result = x * y
        case "/":
            result = x / y

    print(float(result))

main()