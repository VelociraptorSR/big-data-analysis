"""
Write a program that checks whether a positive integer entered by the user is a prime number.

Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
Sample Input: 17
Sample Output: 17 is a prime number.
"""

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False            
    return True
def get_valid_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Error: Input must be a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
def main():
    while True:
        number = get_valid_positive_int("Please enter a positive integer: ")
        if is_prime_number(number):
            print(f"{number} is a prime number.\n")
        else:
            print(f"{number} is not a prime number.\n")
        print("_" * 80)
        print("Choose an option:\n1. Check another number\n2. Exit\n")
        while True:
            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice in (1, 2):
                    break
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")

        if choice == 2:
            print("\nThank you for using the Prime Number Checker!")
            print("Exiting the program...")
            break
            
        print("\n" + "=" * 80)

if __name__ == "__main__":
    print("*" * 80)
    print(f"{' Prime Number Checker ':^80}")
    print("-" * 80)
    main()