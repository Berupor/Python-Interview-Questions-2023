# OOP

### 🔶 1. Explain the basic principles of OOP.

---
#### Answer:
Object-oriented programming (OOP) is a programming paradigm that uses objects, which are instances of classes, to represent and manipulate data. The basic principles of OOP include encapsulation, inheritance, and polymorphism.
### 🔶 2. Are you familiar with SOLID? Look at the code, are there any SOLID principles violated here? How can this be fixed?

---
#### Answer:
SOLID is a set of five principles for object-oriented software design, which stands for Single responsibility, Open-closed, Liskov substitution, Interface segregation, and Dependency Inversion.

### Example:
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof!")
    def fetch(self):
        print("Fetching...")
    def playDead(self):
        print("Playing dead...")
    def rollOver(self):
        print("Rolling over...")
    def chaseTail(self):
        print("Chasing tail...")
        
# This class violates the Single Responsibility Principle as it has too many methods which are doing different tasks.
```
It can be fixed by splitting the class into multiple classes each with a single responsibility

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof!")

class Tricks:
    def fetch(self):
        print("Fetching...")
    def playDead(self):
        print("Playing dead...")
    def rollOver(self):
        print("Rolling over...")
    def chaseTail(self):
        print("Chasing tail...")

```
### 🔶 3. What OOP patterns are you familiar with?

---
#### Answer:

Some common OOP patterns include:
- Singleton pattern: which ensures that a class has only one instance
- Factory pattern: which creates objects without specifying the exact class of object that will be created
- Decorator pattern: which allows behavior to be added to an individual object, either statically or dynamically
- Observer pattern: which allows objects to be notified of changes to other objects
### 🔶 4. How is an interface different from an abstract class?

---
#### Answer:
An interface is a collection of abstract methods (methods with no implementation) that a class must implement. An abstract class is a class that contains one or more abstract methods, but may also have implemented methods. An interface defines a contract, but an abstract class can provide a partial implementation.
### 🔶 5. What are class methods defined through the @classmethod decorator? What are they needed for?

---
#### Answer:
Class methods are methods that are bound to the class and not the instance of the object. They are defined using the @classmethod decorator and take the class as the first argument instead of self. They are useful for creating alternative constructors for a class.

### Example:
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    @classmethod
    def create_from_tuple(cls, name_breed_tuple):
        return cls(*name_breed_tuple)

dog = Dog.create_from_tuple(("Fido", "Golden Retriever"))
print(dog.name)
```
### 🔶 6. How are private attributes declared in Python?

---
#### Answer:
In Python, private attributes are denoted by a double leading underscore. This is a convention indicating that the attribute should not be accessed directly from outside the class, although it can still be accessed if necessary.

### Example:
```python
class Dog:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
    def get_name(self):
        return self.__name
    def get_breed(self):
        return self.__breed

dog = Dog("Fido", "Golden Retriever")
print(dog.__name)  # This will raise an AttributeError
print(dog.get_name())  # This will return "Fido"
```
### 🔶 7. What is MRO in Python?

---
#### Answer:
The Method Resolution Order (MRO) is the order in which the interpreter looks for methods in a class hierarchy. In Python, the MRO is determined by C3, which is a linearization algorithm that finds the order of methods that avoids diamond problem and provide a consistent method resolution order. It works by first determining the depth of the class, and then the order of classes by checking the left-most class first, and then moving to the right.

### Example:
```python
class A:
    def method(self):
        print("Class A method")

class B(A):
    pass

class C(A):
    def method(self):
        print("Class C method")

class D(B, C):
    pass

d = D()
d.method() # Output: "Class C method"
```
in the above example, python interpreter first look for the method in class D, it's not present then it looks in class B which also not present then it looks in class C and it found the method there so it will use this method.

You can use the built-in help function to check the MRO of a class, it prints the order of classes that Python will look through when searching for a method.
```python
help(D)
```
This will output something like
```python
class D(B, C)
 |  Method resolution order:
 |      D
 |      B
 |      C
 |      A
```
It lists the classes in the order that Python will look for methods in them.

### <a href="#top"> Back to top ⬆️</a>

