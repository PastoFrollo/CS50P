def grocery_list():
    i = 0
    while i < len(items):
        print(items.count(items[i]), items[i])
        i = i + items.count(items[i])
    items.clear()


items = []
while True:
    try:
        item = input("Item: ").upper()
    except EOFError:
        grocery_list()
    else:
        items.append(item)
        items.sort()