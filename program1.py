balance = 0
transaction = []
id = 000000 
password = "123456"
attempts = 0
    
while attempts < 3 :
    idx = int(input("Enter your ID: "))
    passwordX = input("Enter your password: ")
    
    if passwordX == password and idx == id:
        proceed = True
        break
        
    else:
        print("Incorrect ID or Password! Try again.")
        print("Attempts left: ", 2 - attempts)
        attempts += 1
        proceed = False

while proceed:
    print("\n1.Deposit")
    print("\n2.Withdraw")
    print("\n3.Check Balance")
    print("\n4.Transaction History")
    print("\n5.Exit")
    
    choice = int(input("Enter your choice: "))
    
    if(choice == 1):
        amt = int(input("Enter amount to deposit: "))
        balance += amt 
        transaction.append("Deposited: " + str(amt))
        print("Amount deposited successfully!")
    
    elif(choice == 2):
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            transaction.append("Withdrawn: " + str(amt))
            print(f"{amt} Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")
    
    elif(choice == 3):
        print("Current balance: ", balance)
    
    elif(choice == 4):
        print("Transaction History: ")
        if len(transaction) == 0:
            print("No transactions yet.")
        else:
            for t in transaction:
                print(t)
    elif(choice == 5):
        print("Thank you for using our service!")
        proceed = False
        break
    else:
        print("Invalid choice! Please try again.")