number1 = 10
number2 = 5
symbols = ['+', '-', '*']
result = int()
operation = ''

for i in symbols:
    if i == '+':
        operation = 'addition'
        result = number1 + number2
        print(f"{operation} of {number1} and {number2} is {result}")
    elif i == '-':
        operation = 'subtraction'
        result = number1 - number2
        print(f"{operation} of {number1} and {number2} is {result}")
    elif i == '*':
        operation = 'multiplication'
        result = number1 * number2
        print(f"{operation} of {number1} and {number2} is {result}")


