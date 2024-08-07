# Python Object-Oriented Programming (OOP) from scratch and focus on creating reusable Python code. 
## modules: Basics, Intermediate, and Advanced. Each module will build upon the previous one, gradually increasing in complexity.

### Module 1: Basics


**Objective:** Understand the fundamental concepts of OOP and how to use classes and objects in Python.

1. **Introduction to OOP**
   - What is Object-Oriented Programming?
   - Key Concepts: Class, Object, Method, Attribute

2. **Classes and Objects**
   - Defining a Class
   - Creating Objects
   - Instance Variables
   - Instance Methods

3. **Basic Inheritance**
   - Inheriting from a Base Class
   - Overriding Methods
   - Calling Parent Class Methods

4. **Encapsulation**
   - Private and Public Attributes
   - Getter and Setter Methods

5. **Simple Example Project**
   - Create a basic `Person` class
   - Define attributes like `name` and `age`
   - Add methods to print details and celebrate birthday

**Sample Code:**

```python
# Basics: Define a Class and Create Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# Create Objects
person1 = Person("Alice", 30)
person1.celebrate_birthday()
```

### Module 2: Intermediate

**Objective:** Dive deeper into OOP concepts, including advanced inheritance, composition, and polymorphism.

1. **Advanced Inheritance**
   - Multiple Inheritance
   - Method Resolution Order (MRO)
   - `super()` Function

2. **Composition**
   - Using Other Objects as Attributes
   - Implementing Composition vs. Inheritance

3. **Polymorphism**
   - Method Overloading (Using Default Arguments)
   - Operator Overloading

4. **Abstract Classes and Interfaces**
   - Defining Abstract Classes
   - Implementing Abstract Methods
   - Using `abc` Module

5. **Intermediate Example Project**
   - Create a `Vehicle` class hierarchy with `Car` and `Bike` subclasses
   - Use composition to add features like `Engine`
   - Implement method overriding and polymorphism

**Sample Code:**

```python
from abc import ABC, abstractmethod

# Intermediate: Abstract Classes
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

# Polymorphism Example
vehicles = [Car(), Bike()]
for vehicle in vehicles:
    vehicle.start_engine()
```

### Module 3: Advanced

**Objective:** Explore advanced OOP concepts and design patterns, and apply them to create robust and reusable code.

1. **Design Patterns**
   - Singleton Pattern
   - Factory Pattern
   - Strategy Pattern

2. **Decorators and Metaclasses**
   - Understanding Decorators
   - Using Metaclasses for Class Creation

3. **Error Handling and Custom Exceptions**
   - Creating Custom Exceptions
   - Raising and Handling Exceptions in OOP Context

4. **Dependency Injection**
   - Implementing Dependency Injection in Python
   - Benefits and Use Cases

5. **Advanced Example Project**
   - Implement a `PaymentProcessing` system with Strategy Pattern
   - Create various payment methods (`CreditCard`, `PayPal`) with common interface
   - Handle custom exceptions for invalid transactions

**Sample Code:**

```python
# Advanced: Strategy Pattern Example
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.process_payment(amount)

# Usage
processor = PaymentProcessor(CreditCardPayment())
processor.make_payment(100)
```

### Summary

- **Module 1 (Basics):** Learn the fundamental concepts of OOP, including classes, objects, and basic inheritance.
- **Module 2 (Intermediate):** Explore advanced inheritance, composition, polymorphism, and abstract classes.
- **Module 3 (Advanced):** Study design patterns, decorators, metaclasses, custom exceptions, and advanced OOP techniques.

