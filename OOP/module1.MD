CerModule 1 of Python Object-Oriented Programming (OOP). We'll cover the basics, including classes, objects, methods, attributes, inheritance, and encapsulation.

### Module 1: Basics of Object-Oriented Programming

#### 1. Introduction to OOP

**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of "objects". Objects are instances of classes and they encapsulate data and behaviors.

**Key Concepts:**
- **Class**: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
- **Object**: An instance of a class. It represents a specific entity with its own state and behaviors.
- **Method**: A function defined within a class that operates on the data (attributes) of the object.
- **Attribute**: A variable that belongs to a class. It represents the state or properties of an object.

#### 2. Classes and Objects

**Defining a Class:**
To define a class in Python, use the `class` keyword followed by the class name and a colon. The class body contains methods and attributes.

**Creating an Object:**
An object is created by calling the class name as if it were a function. This process is called instantiation.

**Example:**

```python
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    # Method to display details
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of the Person class
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

**Explanation:**
- `__init__`: The constructor method initializes the object's attributes.
- `self`: Refers to the instance of the class. It allows access to attributes and methods.

#### 3. Basic Inheritance

**Inheritance** allows a class (child or derived class) to inherit attributes and methods from another class (parent or base class). This promotes code reuse.

**Example:**

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__('Dog')  # Call the constructor of the parent class
        self.name = name

    def make_sound(self):
        print("Woof!")

# Create an object of the Dog class
dog = Dog("Buddy")
dog.make_sound()  # Output: Woof!
```

**Explanation:**
- `super()`: Used to call methods from the parent class.
- `Dog` inherits from `Animal`, but it overrides the `make_sound` method.

#### 4. Encapsulation

**Encapsulation** is the practice of hiding the internal state of an object and requiring all interactions to be performed through methods. It is achieved using private attributes and methods.

**Example:**

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Create an object of the BankAccount class
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
```

**Explanation:**
- Attributes prefixed with `__` are private and cannot be accessed directly outside the class.
- Methods provide controlled access to private attributes.

### Summary

1. **Classes and Objects**:
   - Define a class with `class ClassName`.
   - Instantiate objects using the class name and parentheses.
   - Use `self` to refer to instance attributes and methods.

2. **Basic Inheritance**:
   - Create a parent class and a child class.
   - Use `super()` to call parent class methods from the child class.

3. **Encapsulation**:
   - Use private attributes (with `__`) to protect data.
   - Provide public methods to interact with private data.

