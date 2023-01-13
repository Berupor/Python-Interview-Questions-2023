# Python general questions

### 🔶 1. What is the complexity in O-notation of the len operation of list?

---
#### Answer:
The complexity of the len operation of a list in Python is O(1). This is because the length of a list is stored as a separate attribute, making it a constant-time operation to retrieve the length.

### 🔶 2. And in the O-notation, the difficulty of obtaining an element by index in a list?

---
#### Answer:
The complexity of obtaining an element by index in a list in Python is O(1). This is because lists in Python are implemented as arrays, which allow for constant-time access to elements by index.

### 🔶 3. What is the structure of the implementation of dictionaries? How is the fight against key collisions implemented?

---
#### Answer:
Dictionaries in Python are implemented as a hash table. The fight against key collisions is implemented by using a technique called open addressing, which involves finding the next open slot in the table for a key-value pair that would have otherwise collided with an existing key.

### 🔶 4. How does the Garbage Collector work in Python?

---
#### Answer:
The Garbage Collector in Python works by periodically checking for objects in memory that are no longer being used by the program. Once such objects are identified, they are deallocated and their memory is freed up.

### 🔶 5. With what data structure is set implemented?

---
#### Answer:
A set in Python is implemented as a hash table. This allows for fast insertion, deletion and membership tests.

### 🔶 6. What are decorators and how do they work?

---
#### Answer:
Decorators in Python are a way to modify or extend the functionality of a function or class. They are implemented as functions that take another function as an argument and return a new function that usually includes the functionality of the original function.
```
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("hello!")

say_hello()
# Output: 
# Something is happening before the function is called.
# hello!
# Something is happening after the function is called.

```
### 🔶 7. What are generators and how do they work?

---
#### Answer:
Generators in Python are a special type of iterator that allow a programmer to iterate over a sequence of items, without the need to keep the entire sequence in memory. They are implemented as functions that use the "yield" keyword to return an iterator, instead of a list. When a generator function is called, it returns a generator object, which can be used in a for loop or with the next() function to iterate through the generated sequence.
```
def my_gen():
    yield 1
    yield 2
    yield 3

for i in my_gen():
    print(i)
# Output:
# 1
# 2
# 3
```
### 🔶 8. What are context managers and how do they work?

---
#### Answer:
Context managers in Python are used to set up and tear down a context around a block of code. They are implemented using the "with" statement and a context manager object, which has methods such as "enter" and "exit" that are called when the context is entered and exited. This is useful for managing resources such as file and network connections, where it's important to ensure that the resources are properly closed and cleaned up after use. The "with" statement automatically handles the calls to the "enter" and "exit" methods, making it easy to ensure that the resources are properly managed, even in the presence of exceptions.

### <a href="#top"> Back to top ⬆️</a>
