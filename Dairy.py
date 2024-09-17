#Example 1
class Dairy:
    def __init__(self, cow_name, color, liters, age):
        self.cow_name=cow_name
        self.color=color
        self.liters=liters
        self.age=age
    
    def cow_details(self):
        print(f"{self.cow_name}, {self.color}, {self.liters}, {self.age}")

my_cow=Dairy("Lelmet", "Black with white head ", 30, 3)

print("My cow's name is: ", my_cow.cow_name)
print("It is", my_cow.color)
print("It produces ", my_cow.liters, " Liters")
print("and has", my_cow.age, "years")

my_cow.cow_details()


#Example 2
class Student:
    def __init__(self, name, age, score):
        self.name=name
        self.age=age
        self.score=score

    def scores(self):
        print(f"{self.name}, {self.age}, {self.score}")
    
my_scores=Student("James Wilson", 22, 504)

print(my_scores.name)
print(my_scores.age)
print(my_scores.score)

my_scores.scores()



class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def honk(self):
        print("Honk! Honk! ")
my_car=Car("Tesla", "Model s", 2019)

print(my_car.make)
print(my_car.model)
print(my_car.year)

my_car.honk()

