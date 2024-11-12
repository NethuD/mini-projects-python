#banking _program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))  

    if amount > balance:
        print("Insufficient funds") 
        return 0
    elif amount <= 0:  # Change to <= to prevent zero or negative withdrawals
        print("Amount must be greater than 0")
        return 0
    else:
        return amount 

def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("   Banking Programme    ")
        print("************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("************************")
        choice = input("Enter your choice (1-4): ")
 
        if choice == '1':
            show_balance(balance)  # Pass balance to the function

        elif choice == '2':
            balance += deposit()  # Add deposited amount to balance

        elif choice == '3':
            amount_withdrawn = withdraw(balance)
            balance -= amount_withdrawn  
            # Subtract withdrawn amount from balance

        elif choice == '4':
            is_running = False  # Change to False (no quotes)

        else: 
            print("This is not a valid choice")

    print("Thank you. Have a nice day!")

if __name__ == '__main__':  # Correct the __main__ check
    main()
