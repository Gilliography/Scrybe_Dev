#defining the student class
class Student:
    def __init__(self, name,index_no, age,):
        self.name=name
        self.index_no=index_no
        self.age=age

    #methods to display student details
    def display_info(self):
        print(f"Student Name: {self.name} Index No: {self.index_no} Age: {self.age}")

    # Creating an object of the Car class
my_student=Student("Gilbert", 282296, 33)


# Accessing attributes
print("Name:", my_student.name)
print("Index:", my_student.index_no)
print("Age:", my_student.age)


# Calling a method
my_student.display_info()
