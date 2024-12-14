class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def authenticate(self, entered_pin):
        """Authenticate the user by PIN."""
        if entered_pin == self.pin:
            print("Authentication successful!")
            return True
        else:
            print("Incorrect PIN. Please try again.")
            return False

    def check_balance(self):
        """Check the balance."""
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Successfully deposited ${amount}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Successfully withdrew ${amount}.")
        else:
            print("Insufficient balance or invalid amount.")

    def change_pin(self, old_pin, new_pin):
        """Change the PIN of the account."""
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Incorrect PIN. Unable to change PIN.")

    def show_transaction_history(self):
        """Show transaction history."""
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def menu(self):
        """ATM menu interface."""
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(amount)
            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                self.change_pin(old_pin, new_pin)
            elif choice == '5':
                self.show_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


def main():
    # Simulating an ATM with a PIN and initial balance
    atm = ATM(pin="1234", balance=1000)  # Default balance of $1000

    # User authentication
    print("Welcome to the ATM!")
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if atm.authenticate(entered_pin):
            atm.menu()  # Start the ATM operations
            break
        else:
            attempts -= 1
            print(f"You have {attempts} attempts left.")

        if attempts == 0:
            print("Too many failed attempts. Exiting ATM.")
            break


if __name__ == "__main__":
    main()
