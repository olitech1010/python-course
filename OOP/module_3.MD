### Module 3: Advanced Object-Oriented Programming

This module will cover advanced OOP concepts, including design patterns, metaclasses, decorators, and SOLID principles. These topics are essential for writing scalable, maintainable, and robust software.

#### 1. Design Patterns

**Design patterns** are established solutions to common problems in software design. They help you structure your code in a way that is both efficient and easy to maintain. Let's explore three key design patterns: Singleton, Factory, and Observer.

##### **Singleton Pattern**

**Concept**: The Singleton pattern ensures that a class has only one instance throughout the application's lifetime. This is useful when you want to control access to a resource, such as a configuration manager or a database connection.

**Example**:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.data = "Singleton Data"

# Create instances of Singleton
s1 = Singleton()
s2 = Singleton()

# Both instances are the same
print(s1 == s2)  # Output: True
print(s1.data)   # Output: Singleton Data
```

**Use Cases**:
- **Configuration Management**: Ensuring there's only one configuration manager that the entire application uses.
- **Logging**: A single log manager to handle logging across the application.

##### **Factory Pattern**

**Concept**: The Factory pattern provides an interface for creating objects without specifying the exact class of object that will be created. It's useful when the object creation process is complex or when the type of the object created needs to be determined at runtime.

**Example**:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Create factory
factory = AnimalFactory()

# Create animals
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```

**Use Cases**:
- **UI Components**: Creating different UI elements based on user interaction.
- **Document Parsing**: Creating different parsers (e.g., XML, JSON) depending on the document type.

##### **Observer Pattern**

**Concept**: The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. This pattern is often used in event handling systems.

**Example**:

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

# Example usage
subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")  # Output: Received message: Hello Observers! (twice)
```

**Use Cases**:
- **Event Handling Systems**: Like UI button clicks where multiple actions might be performed when a button is clicked.
- **Data Binding**: Automatically updating UI elements when underlying data changes.

#### 2. Metaclasses

**Concept**: A metaclass in Python is a class of a class that defines how a class behaves. A class is an instance of a metaclass. Metaclasses allow you to control the creation of classes, modify their properties, and customize their behavior.

**Example**:

```python
# Define a metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super(Meta, cls).__new__(cls, name, bases, dct)

# Using the metaclass
class MyClass(metaclass=Meta):
    def __init__(self):
        self.value = 10

    def get_value(self):
        return self.value

# Instantiate the class
obj = MyClass()  # Output: Creating class MyClass
print(obj.get_value())  # Output: 10
```

**Use Cases**:
- **Framework Development**: Used in Django ORM for defining models.
- **Dynamic Class Creation**: Customizing classes based on certain conditions.

#### 3. Decorators

**Concept**: Decorators are a way to modify or extend the behavior of functions or methods without changing their actual code. They are often used in logging, access control, caching, etc.

**Example**:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}")

# Call the decorated function
say_hello("Alice")  
# Output:
# Before function call
# Hello, Alice
# After function call
```

**Use Cases**:
- **Logging**: Automatically log function calls.
- **Access Control**: Restrict access to certain functions.
- **Memoization**: Cache the results of expensive function calls.

#### 4. SOLID Principles

The SOLID principles are a set of five design principles that help developers write more maintainable and extendable code.

- **Single Responsibility Principle (SRP)**: A class should have only one reason to change, meaning it should only have one job or responsibility.
- **Open/Closed Principle (OCP)**: Software entities should be open for extension but closed for modification. This means you can add new functionality without changing existing code.
- **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types without altering the correctness of the program.
- **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use. It's better to have small, specific interfaces than large, general-purpose ones.
- **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Example of SRP**:

```python
class Logger:
    def log(self, message):
        print(f"Log: {message}")

class DataProcessor:
    def __init__(self, logger):
        self.logger = logger

    def process_data(self, data):
        # Processing data...
        self.logger.log("Data processed")

# Usage
logger = Logger()
processor = DataProcessor(logger)
processor.process_data("some data")
```

Here, `Logger` is responsible only for logging, while `DataProcessor` is responsible for processing data, adhering to the SRP.

### Advanced Example Project

**Objective**: Create a notification system where different types of notifications (email, SMS) can be sent using the Observer pattern. Use the Factory pattern to create different types of notification objects and apply SOLID principles throughout the design.

**Step-by-Step**:

1. **Define Notification Types**:
    - `EmailNotification`
    - `SMSNotification`

2. **Implement Factory to Create Notifications**:
    - `NotificationFactory`

3. **Apply Observer Pattern**:
    - `NotificationManager` (Subject)
    - `User` (Observer)

**Example**:

```python
# Step 1: Define Notification Types
class EmailNotification:
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification:
    def send(self, message):
        print(f"Sending SMS: {message}")

# Step 2: Implement Factory to Create Notifications
class NotificationFactory:
    def create_notification(self, notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unknown notification type")

# Step 3: Apply Observer Pattern
class User:
    def update(self, message):
        print(f"User received: {message}")

class NotificationManager:
    def __init__(self):
        self._users = []

    def attach(self, user):
        self._users.append(user)

    def detach(self, user):
        self._users.remove(user)

    def notify(self, message):
        for user in self._users:
            user.update(message)

# Usage Example
factory = NotificationFactory()
email_notification = factory.create_notification("email")
sms_notification = factory.create_notification("sms")

notification_manager = NotificationManager()
user1 = User()
user2 = User()

notification_manager.attach(user1)
notification_manager.attach(user2)

# Send notifications
email_notification.send("Hello via Email")
sms_notification.send("Hello via SMS")
notification_manager.notify("Global Notification to All Users")
```

**Key Points**:
- **Factory Pattern**: Used to create different types of notifications.
- **Observer Pattern**: Manages and notifies users of new messages.
- **SOLID Principles**: Ensured by separating responsibilities and using abstractions.

### Summary



In this module, we covered advanced OOP topics such as design patterns, metaclasses, decorators, and the SOLID principles. These concepts are crucial for writing scalable, maintainable, and reusable code. By applying these principles and patterns, you can develop more complex and robust software systems.