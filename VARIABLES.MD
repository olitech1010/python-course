# CLEMENT OLIVES

### What is a Variable?
A variable in Python is essentially a reserved memory location to store values. This means that when you create a variable, you reserve some space in memory. You can use variables to store data and later retrieve or manipulate that data.

### Creating Variables
In Python, you don't need to declare the type of a variable. The type is inferred from the value you assign to the variable. Here’s how you can create variables:

```python
# Integer variable
age = 25

# Float variable
price = 19.99

# String variable
name = "John Doe"

# Boolean variable
is_student = True
```

### Variable Names
- **Must start with a letter or an underscore (_).**
- **Cannot start with a number.**
- **Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).**
- **Are case-sensitive (age, Age, and AGE are three different variables).**

### Example of Valid and Invalid Variable Names:
```python
# Valid variable names
name = "Alice"
_age = 30
price2 = 15.75

# Invalid variable names
2name = "Bob"   # starts with a number
first-name = "John"  # contains a hyphen
```

### Assigning Values to Variables
You can assign values to variables using the equal sign (`=`). You can also reassign a new value to an existing variable:

```python
x = 5  # Assigning an integer value
print(x)  # Output: 5

x = "Hello"  # Reassigning with a string value
print(x)  # Output: Hello
```

### Multiple Assignment
Python allows you to assign values to multiple variables in one line:

```python
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3

# Assign the same value to multiple variables
x = y = z = 10
print(x, y, z)  # Output: 10 10 10
```

### Data Types
The value assigned to a variable determines its data type. Here are some common data types in Python:

- **Integers (`int`)**: Whole numbers without a decimal point.
- **Floating-point numbers (`float`)**: Numbers with a decimal point.
- **Strings (`str`)**: A sequence of characters enclosed in single or double quotes.
- **Booleans (`bool`)**: Represents `True` or `False`.

### Checking the Type of a Variable
You can check the type of a variable using the `type()` function:

```python
x = 10
print(type(x))  # Output: <class 'int'>

y = 10.5
print(type(y))  # Output: <class 'float'>

name = "Alice"
print(type(name))  # Output: <class 'str'>

is_student = True
print(type(is_student))  # Output: <class 'bool'>
```

### Dynamic Typing
Python is a dynamically typed language, which means you can change the type of a variable by assigning a value of a different type:

```python
x = 10  # x is an integer
print(type(x))  # Output: <class 'int'>

x = "Hello"  # Now x is a string
print(type(x))  # Output: <class 'str'>
```

### Summary
- **Variables** are used to store data.
- **Variable names** must follow certain rules (start with a letter or underscore, no spaces or special characters other than underscores).
- **Values can be assigned** and reassigned to variables.
- **Multiple assignments** can be done in a single line.
- **Data types** include integers, floats, strings, and booleans.
- **Dynamic typing** allows variables to change types.

