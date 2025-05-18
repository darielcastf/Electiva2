import random

try:
    n = int(input("Level: "))
    x = random.randint(1, n)
except ValueError:
    n = int(input("Level: "))

while True:
    try:
        answer = int(input("Guess: "))
        if answer > x:
            print("Too large!")
        elif answer < x:
            print("Too small!")
        else:
            print("Just right!")
            break

    except ValueError:
        continue
