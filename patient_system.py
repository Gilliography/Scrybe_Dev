#Example 1
"""#Defining class called patient
class Patient:
    #Constructor to initialize attributes
    def __init__(self, name, residence, age, illness):
        self.name=name
        self.residence=residence
        self.age=age
        self.illness=illness

    #Method to display patient details
    def display_info(self):
        print(f"{self.name}, {self.residence},{self.age}, {self.illness}")

#Object of the Patient class
my_patient=Patient("Andrews", "Lemook ", 24, "Malaria")

#Accessing attributes 
print(my_patient.name)
print(my_patient.residence)
print(my_patient.age)
print(my_patient.illness)

#Calling a method
my_patient.display_info()"""

#Example 2
"""class BankAccount:
    def __init__(self, name, account_no, amount):
        self.name=name
        self.account_no=account_no
        self.amount=amount
    
    def display_details(self):
        print(f"{self.name}, {self.account_no}, {self.amount}")

my_bank=BankAccount("James Scott", 291928, 2000)

print(my_bank.name)
print(my_bank.account_no)
print(my_bank.amount)

my_bank.display_details()"""


#Example 3

class Watch:
    def __init__(self, name, watch_type, price):
        # Initialize the attributes of the Watch class
        self.name = name
        self.watch_type = watch_type
        self.price = price

    def watch1(self):
        # Return a tuple with the attributes of the watch
        return self.name, self.watch_type, self.price
    
class MetalWatch(Watch):
    def __init__(self, name, watch_type, price, color, quality):
        # Initialize the parent class with name, watch_type, and price
        super().__init__(name, watch_type, price)
        # Initialize additional attributes specific to MetalWatch
        self.color = color
        self.quality = quality
    
    def watch1(self):
        # Return a tuple with all attributes including those specific to MetalWatch
        return self.name, self.watch_type, self.price, self.color, self.quality

# Create an instance of MetalWatch with all required attributes
my_metal_watch = MetalWatch("Rolex", "Luxury", 5000, "Silver", "High")

# Print the details of the MetalWatch
print(my_metal_watch.watch1())  # Output: ('Rolex', 'Luxury', 5000, 'Silver', 'High')
