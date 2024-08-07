### Module 2: Intermediate Object-Oriented Programming

In this module, we will dive deeper into OOP concepts, including advanced inheritance, composition, polymorphism, and abstract classes.

#### 1. Advanced Inheritance

**Multiple Inheritance**:
Multiple inheritance allows a class to inherit from more than one parent class. This can be useful, but it can also lead to complexity and should be used with caution.

**Example**:


```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Swimmer:
    def swim(self):
        print("Swimmer is swimming")

class Duck(Bird, Swimmer):
    pass

# Create an object of the Duck class
duck = Duck()
duck.fly()  # Output: Bird is flying
duck.swim() # Output: Swimmer is swimming
```

**Method Resolution Order (MRO)**:
Python uses MRO to determine the order in which base classes are searched when executing a method. This is particularly important with multiple inheritance.

```python
class A:
    def say(self):
        print("A")

class B(A):
    def say(self):
        print("B")

class C(A):
    def say(self):
        print("C")

class D(B, C):
    pass

d = D()
d.say()  # Output: B
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

#### 2. Composition

Composition is a design principle where one class is made up of one or more objects of other classes. It represents a "has-a" relationship.

**Example**:

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car "has-a" Engine

    def start(self):
        self.engine.start()

# Create an object of the Car class
car = Car()
car.start()  # Output: Engine started
```

#### 3. Polymorphism

Polymorphism allows methods to be used interchangeably between different classes. It provides a way to perform a single action in different forms.

**Method Overloading (Using Default Arguments)**:
Python does not support method overloading by default. However, you can achieve similar functionality using default arguments.

**Example**:

```python
class Math:
    def add(self, a, b, c=0):
        return a + b + c

math = Math()
print(math.add(1, 2))      # Output: 3
print(math.add(1, 2, 3))   # Output: 6
```

**Operator Overloading**:
Python allows you to define how operators behave for custom classes.

**Example**:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (4, 6)
```

#### 4. Abstract Classes and Interfaces

Abstract classes cannot be instantiated and are meant to be subclassed. They can define abstract methods that must be implemented by subclasses.

**Using the `abc` Module**:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create objects of the subclasses
dog = Dog()
cat = Cat()
dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!
```

### Intermediate Example Project

**Objective**: Create a `Vehicle` class hierarchy with `Car` and `Bike` subclasses. Use composition to add features like `Engine`. Implement method overriding and polymorphism.

**Example**:

```python
from abc import ABC, abstractmethod

class Engine:
    def start(self):
        print("Engine started")

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name
        self.engine = Engine()

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print(f"{self.name} is driving")
        self.engine.start()

class Bike(Vehicle):
    def drive(self):
        print(f"{self.name} is biking")
        self.engine.start()

# Create objects of the subclasses
car = Car("Toyota")
bike = Bike("Yamaha")
car.drive()  # Output: Toyota is driving
             #          Engine started
bike.drive() # Output: Yamaha is biking
             #          Engine started
```

### Summary

1. **Advanced Inheritance**:
   - Understand multiple inheritance and Method Resolution Order (MRO).
   - Use `super()` to call methods from parent classes.

2. **Composition**:
   - Implement composition to create a "has-a" relationship.
   - Understand the difference between composition and inheritance.

3. **Polymorphism**:
   - Use method overloading with default arguments.
   - Implement operator overloading for custom classes.

4. **Abstract Classes and Interfaces**:
   - Define abstract classes using the `abc` module.
   - Implement abstract methods in subclasses.

With these concepts, you should be able to create more sophisticated and reusable code. Experiment with these techniques and apply them to your own projects to reinforce your understanding. If you have any questions or need further clarification, feel free to ask!