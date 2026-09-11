'''
    Write a program that takes a year as input from the user and checks whether it is a leap year or not.

    Leap Year Criteria: A year is a leap year if it is divisible by 4, except for century years (ending in 00), which must also be divisible by 400.
    Sample Input: 2024
    Sample Output: 2024 is a Leap Year.

'''

def is_leap_year(year): 
    if(year % 4 == 0 and (year % 100 !=0  or year % 400 == 0)):
        return True
    else:
        return False
def main():
    year = 0
    while True:
        if(year <= 0):
            try:
                year = int(input("Please enter a year greater than or equal to 0: "))
            except ValueError:
                print("Invalid input. Please enter a valid year.")
        else:
            break
    if is_leap_year(year):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")
    print("""Choose an option:
1. Check another year
2. Exit""");
    input_choice = int(input("Enter your choice (1 or 2): "))
    if input_choice == 1:
        main()
    elif input_choice == 2: 
        print("Thank you for using the Leap Year Checker!")
        print("Exiting the program...")
print("="*80)
print(f"{'Welcome to the Leap Year Checker!':^80}")
print("="*80)
main();