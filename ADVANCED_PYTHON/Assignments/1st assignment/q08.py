class BankAccount:
    def _init_(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        return "Deposit successful!"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        self.balance -= amount
        return "Withdrawal successful!"

    def display_details(self):
        return f"Account Holder: {self.name}, Balance: ${self.balance}"

# Menu-driven program
accounts = []
while True:
    print("\n1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. Display Account Details\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter account holder's name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        accounts.append(BankAccount(name, initial_deposit))
    elif choice in [2, 3]:
        name = input("Enter account holder's name: ")
        account = next((acc for acc in accounts if acc.name == name), None)
        if account:
            amount = float(input("Enter amount: "))
            if choice == 2:
                print(account.deposit(amount))
            else:
                print(account.withdraw(amount))
        else:
            print("Account not found.")
    elif choice == 4:
        for account in accounts:
            print(account.display_details())
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")