import random


def guess_num():

    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except:
            pass

    while True:
        try:
            num = random.randint(1, level)
            guess = int(input("Guess: "))
            if guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                print("Just right!")
                return
        except:
            pass


guess_num()
