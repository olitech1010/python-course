
# Python for Data Science and Machine Learning: Beginner Section

## Course Project: Analyzing a Movie Dataset

### Project Overview
- **Objective**: Analyze a dataset containing information about movies to extract insights, such as the most popular genres, average ratings, and trends over time.
- **Dataset**: We will use a CSV file containing columns like `title`, `genre`, `release_year`, `rating`, and `budget`.



## 1. Introduction to Python

### What is Python?
- **Definition**: Python is a high-level, versatile programming language known for its readability and simplicity.
- **Relevance**: Widely used in data science due to its extensive libraries and community support.

### Setting Up Your Python Environment
- **Install Anaconda**: 
  - Visit [Anaconda's official website](https://www.anaconda.com/products/distribution).
  - Download the installer for your operating system (Windows, Mac, Linux).
  - Follow the installation instructions to set up Anaconda, which includes Python, Jupyter Notebook, and many useful libraries.
- **Open Jupyter Notebook**: 
  - Launch Anaconda Navigator from your applications.
  - Click on the "Launch" button under Jupyter Notebook.
  - Your default web browser will open with the Jupyter Notebook interface.

### Basic Syntax and Data Types
- **Basic Syntax**: 
  - To print something on the screen, you use the `print()` function.
  ```python
  print("Hello, World!")
  ```
- **Data Types**:
  - **Integers**: Whole numbers (e.g., `5`)
  - **Floats**: Decimal numbers (e.g., `3.14`)
  - **Strings**: Text (e.g., `"Hello"`)
  - **Booleans**: True or False values (e.g., `True`)

### Practical Exercise
- **Task**: 
  - Create a new Jupyter Notebook.
  - Write a Python script that prints your name and the current year.
  ```python
  print("Your Name")
  print(2024)
  ```

---

## 2. Python Fundamentals

### Variables and Operators
- **Variables**: Store data values. 
  - Example:
  ```python
  movie_title = "Inception"
  release_year = 2010
  ```
- **Operators**: Perform operations on variables.
  - Arithmetic: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division)
  - Relational: `==` (equal to), `!=` (not equal to), `>` (greater than), `<` (less than)

### Control Structures
- **If-Else Statements**:
  ```python
  if release_year > 2000:
      print("Released in the 21st century")
  else:
      print("Released in the 20th century")
  ```
- **Loops**: Repeat a block of code multiple times.
  - **For Loop**:
    ```python
    for i in range(5):
        print(i)
    ```

### Functions and Modules
- **Defining Functions**:
  - Functions allow you to reuse code. You define a function using the `def` keyword.
  ```python
  def greet(name):
      return f"Hello, {name}!"
  ```
- **Using Functions**: Call the function and print the result.
  ```python
  print(greet("Alice"))
  ```

### Exception Handling
- **Try-Except Block**: Handle errors gracefully.
  ```python
  try:
      print(1 / 0)
  except ZeroDivisionError:
      print("Cannot divide by zero!")
  ```

### Practical Exercise
- **Task**: Write a function that takes a movie title and release year as arguments and prints a message based on the year.
  ```python
  def movie_info(title, year):
      if year > 2000:
          print(f"{title} was released in the 21st century.")
      else:
          print(f"{title} was released in the 20th century.")
  
  movie_info("Inception", 2010)
  ```

---

## 3. Data Structures in Python

### Lists, Tuples, and Dictionaries
- **Lists**: Ordered collection of items.
  ```python
  genres = ["Action", "Drama", "Comedy"]
  print(genres)
  ```
- **Tuples**: Immutable ordered collection.
  ```python
  movie_info = ("Inception", 2010, 8.8)
  print(movie_info)
  ```
- **Dictionaries**: Key-value pairs.
  ```python
  movie_details = {"title": "Inception", "rating": 8.8}
  print(movie_details)
  ```

### Sets and Arrays
- **Sets**: Unordered collection of unique items.
  ```python
  unique_genres = set(genres)
  print(unique_genres)
  ```
- **Arrays**: Use NumPy for numerical data.
  ```python
  import numpy as np
  budgets = np.array([160000000, 200000000, 80000000])
  print(budgets)
  ```

### Working with Strings
- **String Manipulation**:
  ```python
  title = "Inception"
  print(title.upper())  # Output: INCEPTION
  print(title.lower())  # Output: inception
  print(title[0:3])     # Output: Inc
  ```

### Practical Exercise
- **Task**: Create a list of movie genres and a dictionary containing details of your favorite movie.
  ```python
  genres = ["Action", "Drama", "Comedy"]
  favorite_movie = {
      "title": "Inception",
      "release_year": 2010,
      "rating": 8.8
  }
  print(genres)
  print(favorite_movie)
  ```

---

## 4. File Handling and Input/Output

### Reading and Writing Files
- **Reading a CSV File**:
  ```python
  with open('movies.csv', 'r') as file:
      data = file.readlines()
  for line in data:
      print(line)
  ```

### Working with CSV and JSON Files
- **Using Pandas for CSV**:
  - Pandas is a powerful library for data manipulation and analysis.
  ```python
  import pandas as pd
  movies_df = pd.read_csv('movies.csv')
  print(movies_df.head())
  ```

### Practical Exercise
- **Task**: Load the movie dataset into a Pandas DataFrame and display the first five rows.
  ```python
  import pandas as pd
  movies_df = pd.read_csv('movies.csv')
  print(movies_df.head())
  ```

---

## Conclusion of Beginner Section
- **Recap**: In this section, we covered the basics of Python programming and started our project by analyzing a movie dataset.
- **Next Steps**: Prepare for the Intermediate section where we will dive deeper into data manipulation and visualization techniques.
