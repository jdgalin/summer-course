# Hands-On: Python Conditional Statements - Solutions

These exercises focus on using `if`, `elif`, and `else` statements to control program flow. You'll work with comparison operators, logical operators, and data types from Lesson 1 to make decisions in your code.

---

## Hands-On #1:

---

### Exercise 1: Check if a Number is Positive

**Goal**: Write a program that checks if a number is positive using an `if` statement.

```python
number = 15

if number > 0:
    print("The number is positive")
```

✅ *Check*: Should print "The number is positive" if the number is greater than 0.

---

### Exercise 2: Even or Odd

**Goal**: Check if a number is even or odd using `if` and `else`.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

✅ *Check*: Should print "Even" or "Odd" based on the number.

---

### Exercise 3: Age Category

**Goal**: Use `if`, `elif`, and `else` to categorize a person by age.

```python
age = 25

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
```

✅ *Check*: Should print the correct category based on age.

---

### Exercise 4: Compare Two Numbers

**Goal**: Compare two numbers and print which is larger, or if they're equal.

```python
a = 10
b = 20

if a > b:
    print("a is larger")
elif b > a:
    print("b is larger")
else:
    print("a and b are equal")
```

✅ *Check*: Should print "a is larger", "b is larger", or "a and b are equal".

---

### Exercise 5: Grade Converter

**Goal**: Convert a numeric grade to a letter grade.

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

✅ *Check*: Should print the correct letter grade.

---

### Exercise 6: String Length Check

**Goal**: Check if a string has more than 10 characters.

```python
text = "Hello, Python!"

if len(text) > 10:
    print("Long string")
else:
    print("Short string")
```

✅ *Check*: Should print "Long string" if length > 10, else "Short string".

---

### Exercise 7: Logical AND Operator

**Goal**: Check if a number is between 10 and 20 (inclusive) using the `and` operator.

```python
number = 15

if number >= 10 and number <= 20:
    print("Number is in range")
else:
    print("Out of range")
```

✅ *Check*: Should print "Number is in range" if between 10 and 20, else "Out of range".

---

### Exercise 8: Logical OR Operator

**Goal**: Check if a character is a vowel using the `or` operator.

```python
letter = "e"

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
else:
    print("Consonant")

# Alternative solution using 'in'
if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```

✅ *Check*: Should print "Vowel" if the letter is a, e, i, o, or u, else "Consonant".

---

### Stretch:  Exercise 9: Leap Year Checker

**Goal**: Determine if a year is a leap year.

```python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

✅ *Check*: Should print "Leap year" or "Not a leap year".

---

### Stretch:  Exercise 10: Nested Conditionals - BMI Calculator

**Goal**: Calculate BMI category using nested `if` statements.

```python
weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"BMI: {bmi:.1f} - Underweight")
elif bmi < 25:
    print(f"BMI: {bmi:.1f} - Normal weight")
elif bmi < 30:
    print(f"BMI: {bmi:.1f} - Overweight")
else:
    print(f"BMI: {bmi:.1f} - Obese")
```

✅ *Check*: Should calculate BMI and print the correct category.

---
## Hands-On #2:
---

### Exercise 11: Create and Print a List

**Goal**: Create a list of your favorite colors and print each color using a `for` loop.

```python
colors = ["red", "blue", "green"]

for color in colors:
    print(color)
```

✅ *Check*: Each color should be printed on a separate line.

---

### Exercise 12: List Length

**Goal**: Create a list of numbers and print how many items are in the list.

```python
numbers = [5, 10, 15, 20, 25]

print(f"The list has {len(numbers)} items")
```

✅ *Check*: Should print "The list has 5 items".

---

### Exercise 13: Append to a List

**Goal**: Start with an empty list and add 5 different items to it using `append()`.

```python
my_list = []

my_list.append("apple")
my_list.append(42)
my_list.append(True)
my_list.append(3.14)
my_list.append("hello")

print(my_list)
print(f"List now has {len(my_list)} items")
```

✅ *Check*: List should contain 5 items after appending.

---

### Exercise 14: Loop Through a Range

**Goal**: Use a `for` loop with `range()` to print numbers 1 through 10.

```python
for i in range(1, 11):
    print(i)
```

✅ *Check*: Should print numbers 1, 2, 3, ..., 10.

---

### Exercise 15: Sum Numbers in a List

**Goal**: Calculate the sum of all numbers in a list using a `for` loop.

```python
numbers = [4, 7, 2, 9, 12]

total = 0
for num in numbers:
    total += num

print(f"The total sum is: {total}")
```

✅ *Check*: Should print the total sum: 34.

---

### Exercise 16: List Membership

**Goal**: Check if a fruit is in a list of available fruits.

```python
available_fruits = ["apple", "banana", "orange", "mango"]
fruit = "banana"

if fruit in available_fruits:
    print("In stock")
else:
    print("Out of stock")
```

✅ *Check*: Should print "In stock" if fruit is in the list, else "Out of stock".

---

### Exercise 17: Count Even Numbers

**Goal**: Count how many even numbers are in a list using a `for` loop.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1

print(f"There are {count} even numbers")
```

✅ *Check*: Should print "There are 5 even numbers".

---

### Exercise 18: While Loop Countdown

**Goal**: Use a `while` loop to count down from 10 to 1.

```python
count = 10

while count >= 1:
    print(count)
    count -= 1
```

✅ *Check*: Should print 10, 9, 8, ..., 2, 1.

---

### Stretch: Exercise 19: While Loop with Condition

**Goal**: Use a `while` loop to keep doubling a number until it exceeds 100.

```python
number = 1

while number <= 100:
    print(number)
    number *= 2
```

✅ *Check*: Should print: 1, 2, 4, 8, 16, 32, 64.

---

### Stretch: Exercise 20: Create a List with Range

**Goal**: Use `range()` to create a list of even numbers from 0 to 20.

```python
even_numbers = []
for i in range(0, 21, 2):
    even_numbers.append(i)

print(even_numbers)

# Alternative using list()
even_numbers = list(range(0, 21, 2))
print(even_numbers)
```

✅ *Check*: Should create [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

---
## Hands-On #3:
---

### Exercise 21: Build a List with Loop

**Goal**: Create a new list containing the squares of numbers 1 through 5.

```python
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

print(squares)
```

✅ *Check*: Should create [1, 4, 9, 16, 25].

---

### Exercise 22: Count Vowels in String

**Goal**: Count how many vowels are in a string using a loop.

```python
text = "Hello World"
vowels = "aeiouAEIOU"

count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
```

✅ *Check*: Should count and print the number of vowels.

---

### Exercise 23: Find Maximum in List

**Goal**: Find the largest number in a list using a `for` loop.

```python
numbers = [23, 67, 12, 89, 45, 34]

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print(f"The maximum is {max_num}")
```

✅ *Check*: Should print "The maximum is 89".

---

### Exercise 24: Break Statement

**Goal**: Loop through a list and stop when you find the number 7.

```python
numbers = [2, 5, 7, 10, 15]

for num in numbers:
    if num == 7:
        break
    print(num)

print("Loop stopped")
```

✅ *Check*: Should print 2, 5, then stop before printing 7.

---

### Exercise 25: Continue Statement

**Goal**: Print numbers 1 to 10 but skip multiples of 3 using `continue`.

```python
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
```

✅ *Check*: Should skip 3, 6, 9 and print all other numbers.

---

### Exercise 26: Nested Loops - Multiplication Table

**Goal**: Use nested `for` loops to create a 3x3 multiplication table.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()  # Empty line after each row

# Alternative - compact format
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3}", end=" ")
    print()  # New line after each row
```

✅ *Check*: Should print products for 1×1 through 3×3.

---

### Exercise 27: While Loop with User Input Simulation

**Goal**: Use a `while` loop to add numbers to a list until the sum exceeds 50.

```python
numbers = [5, 10, 8, 15, 12, 7]

result = []
total = 0
i = 0

while total <= 50 and i < len(numbers):
    result.append(numbers[i])
    total += numbers[i]
    i += 1

print(f"Final list: {result}")
print(f"Total sum: {total}")
```

✅ *Check*: Should stop adding when sum > 50 and print the final list.

---

### Exercise 28: Find Index of Item

**Goal**: Loop through a list to find the index position of a specific item.

```python
fruits = ["apple", "banana", "cherry", "date"]
target = "cherry"

for i in range(len(fruits)):
    if fruits[i] == target:
        print(f"{target} is at index {i}")
        break
```

✅ *Check*: Should print "cherry is at index 2".

---

### Stretch: Exercise 29: Reverse a List Manually

**Goal**: Create a new list that is the reverse of the original using a loop.

```python
original = [10, 20, 30, 40, 50]

reversed_list = []
for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])

print(reversed_list)

# Alternative using while loop
reversed_list = []
i = len(original) - 1
while i >= 0:
    reversed_list.append(original[i])
    i -= 1

print(reversed_list)
```

✅ *Check*: Should create [50, 40, 30, 20, 10] without using `reverse()` or slicing.

---

### Stretch: Exercise 30: Stop After Printing Asterisks

**Goal**: Use nested loops to print asterisks in rows, but stop completely after printing exactly 10 asterisks total.  The number of asterisks in row `n` should be `n`.

```python
num_asterisks = 10
total_printed = 0
row = 1

while total_printed < num_asterisks:
    for col in range(row):
        if total_printed >= num_asterisks:
            break
        print("*", end="")
        total_printed += 1
    print()  # New line after each row
    row += 1

# Alternative using flag variable
num_asterisks = 10
total_printed = 0
stop = False

for row in range(1, 100):  # Use a large range
    if stop:
        break
    for col in range(row):
        print("*", end="")
        total_printed += 1
        if total_printed >= num_asterisks:
            stop = True
            break
    print()
```

✅ *Check*: Should print exactly 10 asterisks total before stopping (e.g., 1 star, then 2 stars, then 3 stars, then 4 stars = 10 total).

---
