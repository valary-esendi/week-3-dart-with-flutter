
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private variable
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance  # Controlled access to private variable


# Example Usage
account = BankAccount("01262003")
account.deposit(1000)
account.withdraw(300)
print(f"Account balance is: ${account.get_balance()}")