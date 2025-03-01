def coke():
    coke_price = 50

    while coke_price > 0:
        print(f"Amount Due: {coke_price}")
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            coke_price = coke_price - coin
            if coke_price <= 0:
                print(f"Change Owed: {abs(coke_price)}")


coke()
