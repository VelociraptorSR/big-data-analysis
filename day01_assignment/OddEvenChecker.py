"""
    Write a program that prompts the user for an integer and prints whether it is even or odd.

    Sample Input: 7
    Sample Output: 7 is an Odd number.
"""
def is_even_number(number):
    if number % 2 == 0:
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
        if is_even_number(number):
            print(f"{number} is a even number.\n")
        else:
            print(f"{number} is not a odd number.\n")
        print("-" * 80)
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
            print("\nThank you for using the Even or Odd Number Checker!")
            print("Exiting the program...")
            break
            
        print("\n" + "=" * 80)

if __name__ == "__main__":
    print("*" * 80)
    print(f"{' Even or Odd Number Checker ':^80}")
    print("-" * 80)
    main()