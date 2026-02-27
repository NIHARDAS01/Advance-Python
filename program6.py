accounts = [
    [101, "Paritosh", 1234, 5000],
    [102, "Suprit", 4321, 3000],
    [103, "Piyush", 1111, 7000]
]

acc_no = int(input("Enter Account Number: "))
pin = int(input("Enter PIN: "))

for account in accounts:
    if account[0] == acc_no and account[2] == pin:
        print("Login Successful!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print("Balance:", account[3])
        
        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            account[3] += amount
            print("Updated Balance:", account[3])
        
        elif choice == 3:
            amount = int(input("Enter withdraw amount: "))
            if amount <= account[3]:
                account[3] -= amount
                print("Updated Balance:", account[3])
            else:
                print("Insufficient Balance")
        
        break
else:
    print("Invalid Account or PIN")