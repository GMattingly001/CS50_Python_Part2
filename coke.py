def main():
    coke(50)
    print()
    coke(25)

def coke(amount_due):
    change_owed = 0
    coins = [25, 10, 5]
    print(f"Amount Due: {amount_due}" )

    while amount_due > 0:
        payment = int(input("Insert Coin: "))
        for coin in coins:
            if payment == coin and payment < amount_due:
                amount_due -= payment
                print(f"Amount Due: {amount_due}")
            elif payment == coin and payment > amount_due:
                change_owed = payment - amount_due
                amount_due -= payment
            elif payment == coin and payment == amount_due:
                amount_due -= payment
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()