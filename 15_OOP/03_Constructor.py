# Constructor : A constructor is a special method that automatically runs when an object is created. In Python, the constructor is: __init__()
class Student:

    # Constructor
    # It runs automatically when an object is created
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display student information
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating an object
# The constructor automatically receives these values
student1 = Student("Shivsai", 21, "CSE AIML")

# Display information
student1.display()



"""When we write:
student1 = Student("Shivsai", 21, "CSE AIML")
Python automatically calls:
__init__("Shivsai", 21, "CSE AIML")"""