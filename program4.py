balance = 0
transaction = []


def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    transaction.append(f"Deposited: {amount}")
    print("Amount Deposited Successfully")


def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        transaction.append(f"Withdrawn: {amount}")
        print("Please collect your cash")
    else:
        print("Insufficient Balance")


def check_balance():
    print("Your current balance is:", balance)


def show_transactions():
    print("\n--- Transaction History ---")
    if len(transaction) == 0:
        print("No transactions yet")
    else:
        for t in transaction:
            print(t)


def menu():
    while True:
        print("\n--- ATM MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            show_transactions()
        elif choice == 5:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice, please try again")

menu()