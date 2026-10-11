# Method Overriding : Method overriding happens when a child class provides its own version of a method that already exists in the parent class.
# Parent class
class Animal:

    def sound(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):

    # Overriding the sound() method
    def sound(self):
        print("Dog barks")


# Another child class
class Cat(Animal):

    # Overriding the sound() method
    def sound(self):
        print("Cat meows")


# Creating objects
dog1 = Dog()
cat1 = Cat()

# Each object uses its own version of sound()
dog1.sound()
cat1.sound()

"""The parent has:

sound()

Dog changes it to:

sound()

and Cat also changes it to:

sound()

This is called method overriding."""