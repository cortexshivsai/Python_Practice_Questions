# Class Variables: A class variable is shared by all objects of the class.
class Student:

    # Class variable
    # Same for every student
    college = "ABC Engineering College"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)


# Creating objects
student1 = Student("Shivsai", 21)
student2 = Student("Rahul", 20)

print("Student 1:")
student1.display()

print()

print("Student 2:")
student2.display()



"""Difference:
Instance Variable	Class Variable
Belongs to each object	Shared by all objects
Usually uses self	Defined directly inside class
Example: self.name	Example: college"""