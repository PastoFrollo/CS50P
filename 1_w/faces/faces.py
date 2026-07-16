def main():
    text = input()
    convert(text)

def convert(emoticon):
    if emoticon == ":)":
        print("🙂")
    elif emoticon == ":(":
        print("🙁")
    else:
        print(emoticon)

main()