#defining class cows
class Cows:
    def __init__(self, name, liters):
        self.name=name
        self.liters=liters
    def display_info(self):
        print(f"{self.name} {self.liters}")

my_cow=Cows ("Cheboit", "200 liters")

print("The cow's name is", my_cow.name)
print("The liters produced are:", my_cow.liters)