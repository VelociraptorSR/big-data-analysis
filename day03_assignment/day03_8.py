'''
De-duplicating Shopping Cart
Scenario: An online shopping cart has duplicate items due to double-clicks: 
["apple", "banana", "apple", "orange", "banana", "banana"]. 
Write a program that processes the list and removes all duplicate items, 
but keeps the first occurrence of each item in its original order. Print the cleaned cart.

Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange']
'''
list_1 = ["apple", "banana", "apple", "orange", "banana", "banana"]
list_2 = sorted(list(set(list_1)))
print(list_2)