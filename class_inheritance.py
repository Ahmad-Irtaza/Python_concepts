class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.roll_number}")

person1 = Person(name="Irtaza", age=19)
student1 = Student(name="Butt", age=18, roll_number="22p-9316")

print("Information about Person 1:")
person1.display_info()

print("\n")

print("Information about Student 1:")
student1.display_info()
