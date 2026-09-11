"""
    Basic Operator Calculator
    Create a program that takes two numbers and a math operator (+, -, *, /) from the user,
    performs the corresponding calculation, and prints the result.

    Sample Input: num1=15, num2=3, operator='/'
    Sample Output: Result: 5.0
"""


def divisionOperation(num1, num2):
    return num1 / num2


def multiplicationOperation(num1, num2):
    return num1 * num2


def substractionOperation(num1, num2):
    return num1 - num2


def addtionOperation(num1, num2):
    return num1 + num2


def userChooice():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    return num1, num2, operator


def main():
    num1, num2, operator = userChooice()

    if operator == "+":
        result = addtionOperation(num1, num2)

    elif operator == "-":
        result = substractionOperation(num1, num2)

    elif operator == "*":
        result = multiplicationOperation(num1, num2)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return

        result = divisionOperation(num1, num2)

    else:
        print("Invalid operator")
        return

    print("Result:", result)


main()