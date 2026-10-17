# Create a program that asks for two numbers and prints their sum, difference, product, and quotient.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

total = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined"

print(f"Sum: {total}, Difference: {difference}, Product: {product}, Quotient: {quotient}")
