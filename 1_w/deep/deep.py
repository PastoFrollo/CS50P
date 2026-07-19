question = input("What is the Answer to the Great Question of Lide: the Universe: or Everything? ").lower()

match question:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")