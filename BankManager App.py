class BankManager:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def display_info(self):
        print(f"The balance for the account holder {self.account_holder_name} (Account No: {self.account_number}) is {self.balance}")

account_number = int(input("Enter your account number here:"))
account_holder_name = input("Enter your name: ")
balance = float(input("Enter your account balance:"))

bankManager = BankManager(account_number, account_holder_name, balance)
bankManager.display_info()
