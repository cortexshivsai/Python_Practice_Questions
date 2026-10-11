# Inheritance :Inheritance means one class can use the properties and methods of another class.The existing class is called the parent/base class.The new class is called the child/derived class.
# Parent class
class Animal:

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


# Child class
# Dog inherits from Animal
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


# Creating object of Dog
dog1 = Dog()

# Dog has its own method
dog1.bark()

# Dog can also use methods inherited from Animal
dog1.eat()
dog1.sleep()

"""What happened?

Dog didn't define eat() or sleep().

But because:

class Dog(Animal):

Dog inherits them from Animal.

So:
Animal
   ↓
  Dog"""