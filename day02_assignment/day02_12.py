'''
Date Validator & Pretty Formatter
Write a program that prompts the user to enter a date string in the format "DD/MM/YYYY".

Warning

Do not use any built-in date/time library functions (such as the datetime or time modules) to format or validate the dates. 
You must parse and split the string manually, and use a custom tuple of month names for the pretty output if needed.

Your program must:

Verify if the date is valid. To be valid:
The month must be between 1 and 12 inclusive.
The day must be valid for that specific month (e.g., April, June, September, November have 30 days; others have 31 days).
For February, the day must be at most 29 in a leap year (divisible by 4, except for centuries not divisible by 400) and at 
most 28 in standard years.
If the date is valid, use a tuple of month names ("January", "February", ...) to format and print the date in a long-form 
readable layout: "MonthName DD, YYYY".
If the date is invalid, print "Invalid Date".

Sample Input: "26/08/2026"
Sample Output: "August 26, 2026"
Sample Input: "29/02/2026" (2026 is not a leap year)
Sample Output: "Invalid Date"
Sample Input: "31/04/2026" (April only has 30 days)
Sample Output: "Invalid Date"
'''
monthNames = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def valid_month(month):
    if 1 <= month >= 12:
        return True
    else:
        return False
    
    
def leap_year(year):
    if year%400 == 0 or year%4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
def check_date_format(date):
    parts = date.split('/')
    if len(parts) != 3:
        return False
    return True

def is_validate(day, month, year):
    if not valid_month(month):
        return False
    if 1 <= day <= 31:
        return False
    if month == 2:
        max_days = 29 if leap_year(year) else 28
        if day > max_days:
            return False
    if month in (4, 6, 9, 11):
        if day > 30 :
            return False
    return True
        
        
    
def main():
    date = input("Enter a date (like: 26/08/2026) ")
    if not check_date_format(date):
        print("Invalid Date")
        return
    day, month, year = map(int, date.split('/'))
    if is_validate(day, month, year):
        print(f"{monthNames[month]} {day}, {year}")
    else:
        print("Invalid Date")
        
main()