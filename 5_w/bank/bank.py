def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower().strip(',')

    if "hello" in greeting:
        value = 0
    elif greeting.startswith("h"):
        value = 20
    else:
        value = 100

    return value

if __name__ == "__main__":
    main()