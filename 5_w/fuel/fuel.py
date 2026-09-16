import sys

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    X, Y = map(int, fraction.split("/"))
    
    if Y == 0:
        raise ZeroDivisionError
    if X > Y or X < 0:
        raise ValueError
        
    return round((X / Y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()