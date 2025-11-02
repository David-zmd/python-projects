# calculator.py

# This block of code ask the user for two numbers and an operator
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, %, **): ")
num2 = float(input("Enter the second number: "))

# This block of code Perform calculation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
elif operator == '%':
    # Check for modulo by zero
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error! Division by zero."
elif operator == '**':
    result = num1 ** num2
else:
    result = "Invalid operator!"

# Print the result
print(f"The result is: {result}")
