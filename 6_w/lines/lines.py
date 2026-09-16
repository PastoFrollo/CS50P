import sys

if len(sys.argv) == 2:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("File does not exist")
        else:
            i = 0
            for line in lines:
                if line == '' or line.startswith("#"):
                    continue
                else:
                    i += 1
            print(i)
    else:
        print("Not a python file")
else:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    else:
        print("Too much command-line arguments")