def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and start_letter(s) and end_numbers(s):
        return True
    else:
        return False

def length(plate):
    plate = list(plate)
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False
    

def start_letter(plate):
    plate = list(plate)
    if len(plate) >= 2:
        for i in range (2):
            if plate[i].isalpha():
                continue
            else:
                return False
    else:
        print("2")
        return False
    return True
    

def end_numbers(plate):
    plate = list(plate)
    i = 0
    while i < len(plate):
        if plate[i].isalpha():
            i += 1
            continue
        else:
            if plate[i].isnumeric() and int(plate[i]) != 0:
                i += 1
                continue
            else:
                return False
    return True


main()