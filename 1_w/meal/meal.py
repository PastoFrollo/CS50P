def main():
    hour = input("What time is it? ").strip().replace(':', '.')
    time = convert(hour)
    
    if 7 <= time <= 8:
            print("breakfast time")
    elif 12 <= time <= 13:
            print("launch time")
    elif 18 <= time <= 19:
            print("dinner time")



def convert(time):
    time = float(time)
    time = int(time) + (time % 1)/60
    return time



if __name__ == "__main__":
    main()