'''
Grading on a Curve
Scenario: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated test scores. 
Convert them to a list of integers. Using a single list comprehension with conditionals, apply the following curve rules:

If a score is below 50, add 10 points.
If a score is 50 or higher, add 5 points.
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103). 
Print the original and the curved grades.

Sample Input: "45 88 30 98 50"
Sample Output:
Original: [45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]
'''
original = [45, 88, 30, 98, 50]
curved = []
for i in original:
    if i < 50:
        i += 10
        curved.append(i)
        continue
    if i >= 50 and i <= 100:
        if 100-i < 5:
            a = 100-i
            i += a
            curved.append(i)
        else:
            i += 5
            curved.append(i)
            
print(curved)