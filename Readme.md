# Simple Banking System

## Overview
The Simple Banking System is a Python-based program that provides a basic banking functionality. Users can create accounts, check balances, deposit and withdraw money, and exit the system. This project demonstrates the use of core Python concepts such as dictionaries, loops, conditionals, error handling, and user input.

---

## Features
1. **Create Account**
   - Assigns a unique account number.
   - Stores account holder's name and initial deposit amount.

2. **Check Balance**
   - Displays the balance of a specified account.
   - Validates the account number.

3. **Deposit Money**
   - Adds a specified amount to an account balance.
   - Ensures the deposit amount is valid.

4. **Withdraw Money**
   - Deducts a specified amount from an account balance.
   - Ensures sufficient funds are available.

5. **Exit System**
   - Terminates the program cleanly.

---

## Prerequisites
- Python 3.6 or higher installed on your system.
- Basic understanding of Python and its syntax.

---

## Installation
1. Clone or download the project to your local machine.
2. Open the terminal (or command prompt) and navigate to the project directory.
3. Run the program by typing:

   ```bash
   python simple_banking_system.py
   ```

---

## Usage
1. Launch the program by running the Python file.
2. Select an option from the menu by entering the corresponding number.
   - **1:** Create a new account by entering the account holder's name and an initial deposit.
   - **2:** Check the balance of an existing account by entering the account number.
   - **3:** Deposit money into an account by entering the account number and the deposit amount.
   - **4:** Withdraw money from an account by entering the account number and the withdrawal amount.
   - **5:** Exit the system.
3. Follow on-screen instructions for each operation.

---

## Program Structure
- **`accounts` Dictionary:**
  Stores account details in the format:
  ```python
  accounts = {
      account_number: {
          "name": str,
          "balance": float
      }
  }
  ```

- **Functions:**
  - `generate_account_number`: Generates unique account numbers.
  - `create_account`: Handles account creation.
  - `check_balance`: Displays the balance of a specified account.
  - `deposit_money`: Adds money to an account.
  - `withdraw_money`: Deducts money from an account.
  - `display_menu`: Displays the main menu options.

---

## Error Handling
- Ensures valid input for account numbers and monetary values.
- Prevents crashes due to invalid inputs by using `try` and `except` blocks.
- Provides meaningful error messages to guide users.

---

## Testing Scenarios
1. **Create Account:**
   - Verify that accounts are stored correctly with unique account numbers.

2. **Check Balance:**
   - Test with valid and invalid account numbers.

3. **Deposit Money:**
   - Validate successful deposits.
   - Handle errors such as negative or zero deposits.

4. **Withdraw Money:**
   - Ensure sufficient funds are required for successful withdrawals.
   - Handle insufficient funds gracefully.

5. **Exit System:**
   - Confirm the program terminates cleanly.

---

## Example Output
### Menu
```
Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
```

### Sample Interaction
```
python simple_banking_system.py

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 1
Enter account holder's name: Sachin Kohli
Enter initial deposit amount: 5000
Account created successfully! Your account number is 1.

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 3
Enter your account number: 1
Enter amount to deposit: 1000
Deposit successful! New balance: $6000.00

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 2
Enter your account number: 1
Account Holder: Sachin Kohli
Balance: $6000.00

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 2
Enter your account number: 1
Account Holder: Sachin Kohli
Balance: $6000.00

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 1
Enter account holder's name: Shubham Chaudhary
Enter initial deposit amount: 6000
Account created successfully! Your account number is 2.

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 2
Enter your account number: 2
Account Holder: Shubham Chaudhary
Balance: $6000.00

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 3
Enter your account number: 2
Enter amount to deposit: 1000
Deposit successful! New balance: $7000.00

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit
Enter your choice: 4
Enter your account number: 2
Enter amount to withdraw: 8000
Insufficient funds.

Simple Banking System
1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit

Enter your choice: 5
Exiting the system. Thank you for using Simple Banking System!
```

---
## Limitations:

**No Persistent Storage:** 

- Account data is stored in memory and will be lost when the program exits.

**Single User Interface:**

- Only one user can interact with the system at a time.

**Basic Validation:**

- Limited error checking for names and account details.

**No Security Features:**

- No passwords or authentication mechanisms are implemented.

**Limited Scalability:**

- Designed for small-scale usage with a few accounts.
---
## License
This project is released under the MIT License.

---

## Contribution
Feel free to fork this repository and submit pull requests to improve functionality or add new features!

