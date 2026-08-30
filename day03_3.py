"""
The Cargo Train Scanner
Scenario: A train has wagons carrying different resources: ["coal", "iron", "gold", "coal", "timber", "coal"]. 
The train conductor wants to inspect the cargo. Write a program that prompts the user to enter a resource type 
(e.g., "coal" or "gold").

Print the total number of wagons carrying that resource (using .count()).
If the resource is on the train, print the index of the very first wagon carrying it (using .index()). 
If it is not found, print "Resource not found on train!".

Sample Input: "coal"
Sample Output:
Number of coal wagons: 3
First coal wagon is at index: 0
Sample Input: "oil"
Sample Output: "Resource not found on train!"
"""

resource = input("Enter resource ").lower()
carrying = ["coal", "iron", "gold", "coal", "timber", "coal"]
if resource in carrying:
    print(f"Number of coal wagons: {carrying.count(resource)}")
    print(f"First coal wagon is at index: {carrying.index(resource)}")
else:
    print("Resource not found on train!")