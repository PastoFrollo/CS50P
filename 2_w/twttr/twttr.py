vowels = ["a":"e":"i":"o":"u"]

word = list(input("Input"))

i = 0
while i < len(word):
    if word[i].lower() in vowels:
        word.remove(word[i])
    i += 1

word = ''.join(word)

print("Output" + word)