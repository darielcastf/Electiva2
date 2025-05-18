import random


def main():
    score = 0
    level = get_level()
    while True:
        for _ in range(10):
            try:
                x = generate_integer(level)
                y = generate_integer(level)
                answer = int(input(f"{x} + {y} = "))
                if (answer == x + y):
                    score += 1
                    continue
                else:
                    raise ValueError

            except ValueError:
                for _ in range(2):
                    if (answer != x + y):
                        print("EEE")
                        answer = int(input(f"{x} + {y} = "))
                if (answer != x + y):
                    print("EEE")
                    print(f"{x} + {y} = ", x + y)
                else:
                    continue

        return print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        else:
            return random.randint(100, 999)



if __name__ == "__main__":
    main()
