# ATM Machine Simulation

class ATM:
    def _init_(self, pin, balance=0):
        """Initialize ATM with initial PIN, starting balance, and transaction history."""
        self._pin = pin
        self.balance = balance
        self.history = []

    def verify_pin(self, pin):
        """Verify if the provided PIN matches the stored PIN."""
        return pin == self._pin

    def check_balance(self):
        """Return the current balance."""
        return f"Balance: ₹{self.balance}"

    def deposit_cash(self, amount):
        """Deposit amount to balance if amount is positive."""
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: ₹{amount}")
            return f"₹{amount} deposited successfully."
        return "Invalid deposit amount."

    def withdraw_cash(self, amount):
        """Withdraw amount if sufficient funds are available."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew: ₹{amount}")
            return f"₹{amount} withdrawn successfully."
        elif amount > self.balance:
            return "Insufficient funds."
        return "Invalid withdrawal amount."

    def change_pin(self, old_pin, new_pin):
        """Change PIN if the old PIN is verified."""
        if self.verify_pin(old_pin):
            self._pin = new_pin
            self.history.append("PIN changed.")
            return "PIN changed successfully."
        return "Incorrect old PIN."

    def transaction_history(self):
        """Return all transaction history."""
        if not self.history:
            return "No transactions yet."
        return "\n".join(self.history)

# Function to run the ATM simulation
def atm_menu():
    atm = ATM(pin="1234", balance=5000)  # Initialize with default PIN and balance
    print("Welcome to the ATM!")

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Enter option number: ")
        
        if choice == "1":
            pin = input("Enter PIN: ")
            if atm.verify_pin(pin):
                print(atm.check_balance())
            else:
                print("Invalid PIN.")

        elif choice == "2":
            pin = input("Enter PIN: ")
            if atm.verify_pin(pin):
                try:
                    amount = float(input("Enter deposit amount: "))
                    print(atm.deposit_cash(amount))
                except ValueError:
                    print("Invalid input. Enter a numeric value.")
            else:
                print("Invalid PIN.")

        elif choice == "3":
            pin = input("Enter PIN: ")
            if atm.verify_pin(pin):
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    print(atm.withdraw_cash(amount))
                except ValueError:
                    print("Invalid input. Enter a numeric value.")
            else:
                print("Invalid PIN.")

        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            if atm.verify_pin(old_pin):
                new_pin = input("Enter new PIN: ")
                print(atm.change_pin(old_pin, new_pin))
            else:
                print("Incorrect current PIN.")

        elif choice == "5":
            pin = input("Enter PIN: ")
            if atm.verify_pin(pin):
                print("Transaction History:")
                print(atm.transaction_history())
            else:
                print("Invalid PIN.")

        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Please select a valid option.")

# Start the ATM menu
atm_menu()