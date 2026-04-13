balance = 0.0

def display_balance():
    print(f"\nCurrent Balance: Rs. {balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Successfully deposited Rs. {amount}")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    elif amount <= 0:
        print("Invalid amount.")
    else:
        balance -= amount
        print(f"Successfully withdrew Rs. {amount}")

while True:
    print("\n--- BANKING MENU ---")
    print("a) Check Balance")
    print("b) Deposit Money")
    print("c) Withdraw Money")
    print("q) Exit")
    
    choice = input("Select an option: ").lower()
    
    if choice == 'a':
        display_balance()
    elif choice == 'b':
        deposit()
    elif choice == 'c':
        withdraw()
    elif choice == 'q':
        print("Thank you for using our banking system.")
        break
    else:
        print("Invalid option.")
      
