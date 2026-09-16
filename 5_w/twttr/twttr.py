def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = ["a","e","i","o","u"]

    word = list(word)
    
    i = 0
    while i < len(word):
        if word[i].lower() in vowels:
            word.remove(word[i])
            continue

        i += 1

    word = ''.join(word)

    return word

if __name__ == "__main__":
    main()