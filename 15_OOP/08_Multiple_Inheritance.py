# Multiple Inheritance : Multiple inheritance means one child class inherits from more than one parent class.
# First parent class
class Father:

    def father_skill(self):
        print("Father can drive")


# Second parent class
class Mother:

    def mother_skill(self):
        print("Mother can cook")


# Child class inherits from both Father and Mother
class Child(Father, Mother):

    def child_skill(self):
        print("Child can play football")


# Creating object of Child
child1 = Child()

# Method from Father
child1.father_skill()

# Method from Mother
child1.mother_skill()

# Method from Child
child1.child_skill()

"""
Father ─────┐
            ↓
          Child
            ↑
Mother ─────┘

The Child class can access methods from both parent classes."""