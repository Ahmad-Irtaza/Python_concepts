class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"roll_number: {self.roll_number}")

student1 = Student(name="Irtaza", age=20, roll_number="22p-9316")
student2 = Student(name="Butt", age=19, roll_number="22p-9316")

print("Information about Student 1:")
student1.display_info()

print("\nInformation about Student 2:")
student2.display_info()
