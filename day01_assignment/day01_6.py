"""
    Sum of N Natural Numbers. Write a script that accepts a positive integer from the user and
    calculates the sum of all natural numbers up to N.

    Sample Input: N = 10
    Sample Output: Sum: 55
"""


def sumOfNaturalNumber():
    n = int(input("Enter N: "))

    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


def main():
    result = sumOfNaturalNumber()
    print("Sum:", result)


if __name__ == "__main__":
    print("*" * 80)
    print(f"{' Sum of Nth Natural Number ':^80}")
    print("-" * 80)
    main()