class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Ksh.{amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: Ksh.{amount}")
        elif amount > self.__balance:
            print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

# Display current balance
print(f"Current Balance: Ksh.{account.get_balance()}")
