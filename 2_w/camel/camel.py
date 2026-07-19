camelCase = input("camelCase: ")

camelCase = list(camelCase)

i = 0
while i < len(camelCase):
    if camelCase[i].isupper():
        camelCase[i] = f"_{camelCase[i].lower()}"
    i += 1

camelCase = ''.join(camelCase)
print(f"snake_case: {camelCase}")