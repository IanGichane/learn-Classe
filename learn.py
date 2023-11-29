# Encapsulation and Abstraction:

# How does encapsulation contribute to the concept of data hiding in Python's OOP?
# Can you provide an example of how abstraction is achieved in Python through the use of classes and objects?

# helps make attributes private and protected so  that there is only controlled modification

# Bundling data/attributes and functions that operate the data into a single unit called a class
# safegaurding secrets
#Placing the working of a magic trick inside a box.Sheild the internal details

# what is __init__?
     #Is a special is a special method that python runs automatically whenever we create a new instance based on the dog class
          #IT a convention that helps prevent python's default method names from conflicting with your method names
#you use .__init__() to declare which attributes each instance of the class should have


# Public members are available to anyone that can access the class.
# Private members are available to the class that instantiated them.
# Protected members are available to the class that instantiated them and any object that inherits from that 
#       class, but is not accessible otherwise.

    # Encapsulation with the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author #
        self._is_available = True  # Protected attribute(private)

    def borrow_book(self):
        if self._is_available:
            self._is_available = True
            return f"{self.title} by {self.author} has been borrowed."
        else:
            return "Sorry, the book is currently unavailable."

    # Creating an instance of the Book class
my_book = Book("The Pythonic Way", "John Python")

    # Interacting with encapsulated attributes and methods
print(my_book.borrow_book())   # Output: The Pythonic Way by John Python has been borrowed.
print(my_book._is_available)   # Output: False
 
class MyClass:
    def __init__(self):
        self.__private_attribute = 42
        self._protected_attribute = "Hello"

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value

"""
Single Underscore (_) : indicates a protected attribute
Double Underscore (__) : indicates a private attribute - only limited to the class that created it.
No underscore: indicates a public attribute - can be accessed anywhere

"""

# 1.2 Abstraction
# involves hiding the complex implementation details while exposing only the necessary functionalities

    from abc import ABC, abstractmethod

    # Interface Example
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    # Concrete Class Implementing Interface
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2
        
    class triangle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 1/2*b*h

    # Using Abstraction through Interface
    circle = Circle(5)
    print(circle.area()) 

# Code Reusability:

# Inheritance promotes the reuse of code. The subclass inherits attributes and methods from the superclass, reducing redundancy in your code.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

# both Dog and Cat reuse the speak method from the Animal superclass/Parent class

# Extensibility:

# Inheritance allows you to add new features or modify existing ones in a subclass without altering the code in the superclass/child class
class Bird(Animal):
    def fly(self):
        print("I can fly!")

class Parrot(Bird):
    def speak(self):  # Overrides the speak method from Animal
        print("Squawk!")

# Parrot extends the functionality of Bird and overrides the speak method from Animal
# Elijah Ngocho10:41 AM
# Complexity: Multiple inheritance can lead to complex and hard-to-understand code.
# Understanding the flow of control and the origin of methods and attributes becomes more challenging as the number of inherited classes increases.