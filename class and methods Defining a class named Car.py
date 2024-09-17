# Defining a class named Car
class Car:
    # Constructor to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display car details
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)  # Output: 2020

# Calling a method
my_car.display_info()  # Output: 2020 Toyota Corolla