import streamlit as st
from abc import ABC, abstractmethod

#Abstract class for Bank Manager
class account(ABC):
    @abstractmethod
    def display_info(self):
        pass

#Bank Manager class
class BankManager(account):
    def __init__(self, account_number, account_holder_name, balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    #Getter methods for private attributes
    def get_account_number(self):
        return self.__account_number
    
    def get_account_holder_name(self):
        return self.__account_holder_name
    
    def get_balance(self):
        return self.__balance
    
#operations
#deposit function
def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
        print(f"The deposited amount is {amount}. your new balance is {self.__balance}.")
    else:
        print("❌ Deposit amount must be positive.")

#withdrawal function
def withdraw(self, amount):
    if amount > 0 and amount <= self.__balance:
        self.__balance -= amount
        print(f"The amount withdrawn is {amount}. your new balance is {self.__balance}.")
    else:
        print("❌ Insufficient funds.")


#Method overriden in child class
def display_info(self):
    print("\n=== Bank Account Information ===")
    print(f"Account Holder Name: {self.get_account_holder_name()}")
    print(f"Account Number: {self.get_account_number()}")
    print(f"Current Balance: {self.get_balance():.2f}")

#Polymorphism
class PremiumBankManager(BankManager):
    def display_info(self):
        print("\n=== Premium Bank Account Information ===")
        super().display_info()
        print("You are a premium account holder with additional benefits.")

#Menu for user interaction
def bank_manager_menu():
    print("\n=== Welcome To Standard Bank System===")
    account_number = int(input("Enter your account number: "))
    account_holder_name = input("Enter your name: ")
    balance = float(input("Enter your account balance: "))
    account_type = input("Enter account type (standard/premium): ").strip().lower()

    if account_type =="premium":
        bank_manager = PremiumBankManager(account_number, account_holder_name, balance)
    else:
        manager = BankManager(account_number, account_holder_name, balance)

#Menu options
    while True:
        print("\n=== Menu ===")
        print("1. Display Account Info")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            bank_manager.display_info()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            bank_manager.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
        elif choice == '4':
            balance = bank_manager.get_balance()
            print(f"Current Balance: {balance:.2f}")
        elif choice == '5':
            print("Exiting the Bank Manager System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again select (1-5).")
if __name__ == "__main__":
    bank_manager_menu()