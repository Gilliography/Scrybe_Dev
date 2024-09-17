# Define a class called BankAccount to represent a bank account
class BankAccount:
    # Constructor (__init__) method to initialize the account balance
    def __init__(self, balance):
        # The balance attribute is private, indicated by the double underscore '__'
        # This prevents direct access to this attribute from outside the class
        self.__balance = balance

    # Public method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            # Modify the private balance attribute within the class
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            # Modify the private balance attribute within the class
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    # Public method to check the balance of the account
    def get_balance(self):
        # Access the private balance attribute within the class
        return self.__balance

# Create an instance of BankAccount with an initial balance of 1000
account = BankAccount(1000)

# Prompt the user to enter the amount they want to deposit
deposit_amount = float(input("Enter the amount you want to deposit: "))
account.deposit(deposit_amount)  # Deposit the user-input amount into the account

# Prompt the user to enter the amount they want to withdraw
withdraw_amount = float(input("Enter the amount you want to withdraw: "))
account.withdraw(withdraw_amount)  # Withdraw the user-input amount from the account

# Print the current balance using the public method
print(f"Final balance is {account.get_balance()}.")
