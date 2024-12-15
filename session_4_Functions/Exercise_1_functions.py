#Write a Python function called multiply_numbers that takes two arguments
# , num1 and num2. 
# Inside the function, calculate the product of these two numbers 
# and return the result.


def multiply_numbers(num1, num2):
    return num1*num2

def add(a, b):
    return a + b

   
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
result = multiply_numbers(x, y)
print(f"The product of {x} and {y} is {result}")

