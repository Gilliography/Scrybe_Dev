class GradeManager:
    def __init__(self, name, marks, grade):
        self.name = name 
        self.marks = marks
        self.grade = grade

        print(f"Grade Manager initialized for {self.name} with marks {self.marks} and grade {self.grade}.")

name = input("Enter your name:")
marks = int(input("Enter your marks:"))
while True:
    if marks > 100 or marks < 0:
        print("Marks should be between 0 and 100. Please try again.")
    elif marks >=0 and marks <=20:
        grade = "F"
    elif marks > 20 and marks <= 40:
        grade = "D"
    elif marks > 40 and marks <= 60:
        grade = "C"
    elif marks > 60 and marks <= 80:
        grade = "B"
    elif marks > 80 and marks <= 90:
        grade = "A"
    elif marks > 90 and marks <= 100:
        grade = "A+"
    else:
        grade = "Invalid marks"
    break
def main():
    while True:
        try:
            print("\n===Grade Manager Menu===")
            print("1. Enter Student Details")
            print("2. Enter Marks")
            print("3. Exit")

            choice = input("Enter your choice")

            if choice == '1':
                name = input("Enter student's name: ")
                print(f"student's name is {name}.")
            elif choice == '2':
                marks = int(input("Enter student's marks: "))
                print(f"student's marks are {marks}.")
            elif choice == '3':
                print("Exiting Grade Manager. Goodbye!")

grade_manager = GradeManager(name, marks, grade)
print(f"Hi {name}, your grade is: {grade}")