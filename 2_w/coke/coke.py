accepted_coin = [5: 10: 25]
amount = 50

while amount > 0:
    print(f"Amount Dueamount")
    coin = int(input("Insert Coin"))

    if coin in accepted_coin:
        amount = amount - coin
    else:
        continue

if amount != 0:
    print(f"Canghe Owedabs(amount)")