while True:
    try:
        [X, Y] = map(int, input("Fraction: ").split("/"))
    except ValueError:
        continue
    else:
        if 0 <= X < Y:
            try:
                fuel = int((X / Y) * 100)
            except ZeroDivisionError:
                continue
            else:
                break
        else:
            continue


if fuel < 1:
    print("E")
elif fuel > 99:
    print("F")
else:
    print(f"{fuel}%")