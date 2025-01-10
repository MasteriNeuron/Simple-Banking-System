import sys

# Dictionary to store account details
accounts = {}

# Function to generate a unique account number
def generate_account_number():
    return len(accounts) + 1

# Function to create an account
def create_account():
    name = input("Enter account holder's name: ").strip()
    try:
        initial_deposit = float(input("Enter initial deposit amount: "))
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        account_number = generate_account_number()
        accounts[account_number] = {"name": name, "balance": initial_deposit}
        print(f"Account created successfully! Your account number is {account_number}.")
    except ValueError as e:
        print(f"Error: {e}")

# Function to check account balance
def check_balance():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number in accounts:
            print(f"Account Holder: {accounts[account_number]['name']}")
            print(f"Balance: ${accounts[account_number]['balance']:.2f}")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")

# Function to deposit money
def deposit_money():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number in accounts:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            accounts[account_number]['balance'] += amount
            print(f"Deposit successful! New balance: ${accounts[account_number]['balance']:.2f}")
        else:
            print("Account not found.")
    except ValueError as e:
        print(f"Error: {e}")

# Function to withdraw money
def withdraw_money():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number in accounts:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if accounts[account_number]['balance'] >= amount:
                accounts[account_number]['balance'] -= amount
                print(f"Withdrawal successful! New balance: ${accounts[account_number]['balance']:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")
    except ValueError as e:
        print(f"Error: {e}")

# Function to display the menu
def display_menu():
    print("\nSimple Banking System")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_account()
            elif choice == 2:
                check_balance()
            elif choice == 3:
                deposit_money()
            elif choice == 4:
                withdraw_money()
            elif choice == 5:
                print("Exiting the system. Thank you for using Simple Banking System!")
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
