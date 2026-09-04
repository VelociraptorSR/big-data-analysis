"""
    Multiplication Table Generator
    Write a program that takes an integer from the user and prints its multiplication table from 1 to 10.

    Sample Input: 5
    Sample Output:
    5 x 1 = 5
    5 x 2 = 10
    ...
    5 x 10 = 50
"""

from BasciOperatorCalculator import multiplicationOperation 

def createMultiplicationTable():
    number = int(input("Enter a number: "))

    for i in range(1, 11):
        result = multiplicationOperation(number, i)
        print(f"{number} x {i} = {result}")


def main():
    createMultiplicationTable()


if __name__ == "__main__":
    print("*" * 80)
    print(f"{' Multiplication Table Generator ':^80}")
    print("-" * 80)
    main()