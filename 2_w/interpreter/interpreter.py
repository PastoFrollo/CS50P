[x, y, z] = input("Expression: ").split()
x = int(x)
z = int(z)

match y:
    case "+":
        result = x + z
        print(f"{result:.1f}")
    case "-":
        result = x - z
        print(f"{result:.1f}")
    case "*":
        result = x * z
        print(f"{result:.1f}")
    case "/":
        if z != 0:
            result = x / z
            print(f"{result:.1f}")
        else:
            print("Impossible")