"""
    Write a Python script to print the first N terms of the Fibonacci sequence, where N
    is provided by the user.

    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, …
    Sample Input: N = 6
    Sample Output: 0, 1, 1, 2, 3, 5
"""

def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def get_valid_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Error: N must be a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def main():
    while True:
        n = get_valid_positive_int("Please enter a positive integer for N: ")
        fib_seq = fibonacci_sequence(n)
        print(f"The first {n} terms of the Fibonacci sequence are: {', '.join(map(str, fib_seq))}")
        print("_" * 80)
        print("Choose an option:\n1. Generate Another Fibonacci Sequence\n2. Exit\n")
        while True:
            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice in (1, 2):
                    break
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")
        if choice == 2:
            print("\nThank you for using the Fibonacci Sequence Generator!")
            print("Exiting the program...")
            break
        
        print("\n" + "=" * 80)

if __name__ == "__main__":
    print("*" * 80)
    print(f"{' Fibonacci Sequence Generator ':^80}")
    print("-" * 80)
    main()