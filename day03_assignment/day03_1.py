"""
A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]. 
When the wizard steps through a magic portal, two things happen:

A new item enters the bag (prompts the user to input the item name to append to the end).
The oldest item in the bag (at index 0) is dissolved and ejected. 
Write a program to simulate this portal transition and print the final bag contents.

Sample Input: (User inputs "amulet")
Sample Output:
Portal transition activated!
Ejected oldest item: staff
Current items in the magic bag: ['potion', 'spellbook', 'amulet']
"""
bag = ["staff", "potion", "spellbook"]
print("Portal transition activated!")
new_item = input("Enter new item")
print(f"Ejected oldest item: {bag.pop(0)}")
bag.append(new_item)
print(f"Current items in the magic bag: {bag}")