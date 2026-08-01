import random


def main():
    n = get_level()
    generate_problems(n)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1<= n <= 3:
                return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def generate_problems(level):
    score = 0
    for i in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)

        for k in range(3):
            try:
                answer = int(input(f"{X} + {Y} = "))
            except ValueError:
                pass
            else:
                if answer == X + Y:
                    score = score + 1
                    break
                elif k == 2:
                    print(f"Answer: {X + Y}")
    
    print(f"Score: {score}")


if __name__ == "__main__":
    main()