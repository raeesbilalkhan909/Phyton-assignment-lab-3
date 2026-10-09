balance = 50000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("Your balance is:", balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposited:", amount)
            print("New balance:", balance)
        else:
            print("Invalid amount.")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawn:", amount)
            print("New balance:", balance)
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
