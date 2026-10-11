# Polymorphism : Polymorphism means one method/function name can behave differently for different objects.
#A very easy way to understand it is through method overriding.
# Parent class
class Animal:

    def sound(self):
        print("Animal makes a sound")


# Dog class
class Dog(Animal):

    def sound(self):
        print("Dog says: Woof")


# Cat class
class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")


# Create objects
dog1 = Dog()
cat1 = Cat()

# Store different objects in a list
animals = [dog1, cat1]

# Same method name
# But different objects give different results
for animal in animals:
    animal.sound()


"""Notice this:

animal.sound()

We use the same method call.

But:

Dog object → Dog says Woof
Cat object → Cat says Meow

That is polymorphism."""    