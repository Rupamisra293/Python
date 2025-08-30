num = int(print("Enter a number: "))

#if statement
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# Output: The number is positive/negative/zero based on the input

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# Output: The number is even/odd based on the input

#for loop
for i in range(5):
    print(f"Iteration {i}")
# Output: Iteration 0, Iteration 1, Iteration 2, Iteration 3, Iteration 4
#while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
# Output: Count is 0, Count is 1, Count is 2, Count is 3, Count is 4
#function definition
def greet(name):
    return f"Hello, {name}!"
#function call
print(greet("Alice"))
# Output: Hello, Alice!
# Input: 5
# Input: Alice
#list comprehension
squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]
#dictionary usage
person = {"name": "Bob", "age": 30}
print(person["name"])
# Output: Bob
# Input: A number
# Input: A name
#class definition
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
#class instantiation and method call
my_dog = Dog("Buddy")
print(my_dog.bark())
# Output: Buddy says Woof!
# Input: A name for the dog
#exception handling
try:
    result = 10 / num
    print(f"10 divided by {num} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# Output: 10 divided by num is result or Error message if num is 0
# Input: A number (can be zero)
#file operations
with open("example.txt", "w") as file:
    file.write("Hello, World!")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  
# Output: Hello, World!
# Input: None (creates and reads a file)
# Note: Ensure you have write permissions in the directory where this script is run.
# This code demonstrates various Python constructs including conditionals, loops, functions, classes, exception handling, and file operations.
# Note: The code includes input prompts; please provide appropriate inputs when running the script.
