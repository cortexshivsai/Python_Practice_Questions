#Instance Variables : Instance variables are variables that belong to a particular object.Usually they are created using: self.variable
class Student:

    def __init__(self, name, age, marks):
        # Instance variables
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# First object
student1 = Student("Shivsai", 21, 85)

# Second object
student2 = Student("Rahul", 20, 90)

print("Student 1:")
student1.display()

print()

print("Student 2:")
student2.display()


"""Why are these called instance variables?
Because each object has its own values.
student1 → name = Shivsai, marks = 85
student2 → name = Rahul,   marks = 90
Changing student1 does not normally change student2."""