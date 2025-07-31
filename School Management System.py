import json
import os

# Global Constants
SCHOOL_NAME = "Greenwood High School"
DATA_FILE = "school_data.json"

# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {'name': self.name, 'age': self.age}


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = {}  # {subject: grade}

    def to_dict(self):
        data = super().to_dict()
        data.update({'student_id': self.student_id, 'grades': self.grades})
        return data


class Teacher(Person):
    def __init__(self, name, age, username, password):
        super().__init__(name, age)
        self.username = username
        self.password = password
        self.subjects = []  # List of subjects they teach

    def to_dict(self):
        data = super().to_dict()
        data.update({'username': self.username, 'password': self.password, 'subjects': self.subjects})
        return data


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.load_data()

    def save_data(self):
        data = {
            'students': [s.to_dict() for s in self.students],
            'teachers': [t.to_dict() for t in self.teachers],
        }
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                for s in data['students']:
                    student = Student(s['name'], s['age'], s['student_id'])
                    student.grades = s['grades']
                    self.students.append(student)
                for t in data['teachers']:
                    teacher = Teacher(t['name'], t['age'], t['username'], t['password'])
                    teacher.subjects = t['subjects']
                    self.teachers.append(teacher)

    def add_student(self, name, age, student_id):
        student = Student(name, age, student_id)
        self.students.append(student)
        self.save_data()

    def add_teacher(self, name, age, username, password):
        teacher = Teacher(name, age, username, password)
        self.teachers.append(teacher)
        self.save_data()

    def assign_subject_to_teacher(self, username, subject):
        for teacher in self.teachers:
            if teacher.username == username:
                teacher.subjects.append(subject)
                print(f"Assigned {subject} to {teacher.name}")
                self.save_data()
                return
        print("Teacher not found.")

    def grade_student(self, teacher_username, student_id, subject, grade):
        for teacher in self.teachers:
            if teacher.username == teacher_username and subject in teacher.subjects:
                for student in self.students:
                    if student.student_id == student_id:
                        student.grades[subject] = grade
                        print(f"{student.name} graded {grade} in {subject}")
                        self.save_data()
                        return
                print("Student not found.")
                return
        print("Teacher not authorized for this subject.")

    def login_teacher(self, username, password):
        for teacher in self.teachers:
            if teacher.username == username and teacher.password == password:
                return teacher
        return None

    def display_students(self):
        for student in self.students:
            print(f"{student.name} (ID: {student.student_id}) - Grades: {student.grades}")


# ==== MAIN INTERFACE ====
def main():
    school = School()

    while True:
        print(f"\nWelcome to {SCHOOL_NAME}")
        print("1. Admin Login")
        print("2. Teacher Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            admin_panel(school)
        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            teacher = school.login_teacher(username, password)
            if teacher:
                teacher_panel(school, teacher)
            else:
                print("Invalid credentials.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def admin_panel(school):
    while True:
        print("\n--- Admin Panel ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Assign Subject to Teacher")
        print("4. Display Students")
        print("5. Back")
        choice = input("Choose: ")

        if choice == '1':
            name = input("Student Name: ")
            age = int(input("Age: "))
            sid = input("Student ID: ")
            school.add_student(name, age, sid)
        elif choice == '2':
            name = input("Teacher Name: ")
            age = int(input("Age: "))
            uname = input("Username: ")
            pw = input("Password: ")
            school.add_teacher(name, age, uname, pw)
        elif choice == '3':
            uname = input("Teacher Username: ")
            subject = input("Subject to Assign: ")
            school.assign_subject_to_teacher(uname, subject)
        elif choice == '4':
            school.display_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def teacher_panel(school, teacher):
    while True:
        print(f"\n--- Teacher Panel ({teacher.name}) ---")
        print("Subjects:", ", ".join(teacher.subjects))
        print("1. Grade a Student")
        print("2. Back")
        choice = input("Choose: ")

        if choice == '1':
            sid = input("Student ID: ")
            subject = input("Subject: ")
            grade = input("Grade: ")
            school.grade_student(teacher.username, sid, subject, grade)
        elif choice == '2':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
