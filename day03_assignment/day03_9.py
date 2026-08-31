'''
The Josephus Elimination Game
Scenario: A group of N soldiers (numbered 1 to N) stand in a circle. Starting from the first soldier, every Kth soldier 
is eliminated from the circle. The count continues with the next remaining soldier, moving clockwise. 
This process repeats until only one soldier remains. 
Write a program that prompts the user to enter N (number of soldiers) and K (elimination interval). 
Simulate the game using a list and print the order of eliminations and the final survivor.

Sample Input: N = 5, K = 2
Sample Output:
Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
Eliminated soldier: 4 (Remaining: [1, 3, 5])
Eliminated soldier: 1 (Remaining: [3, 5])
Eliminated soldier: 5 (Remaining: [3])
The sole survivor is: 3
'''
soldier = [1, 2, 3, 4, 5]
k = 2
while len(soldier) != 1:
    el_sol = soldier.pop(k-1)
    k += 1
    if k > len(soldier):
        k %= len(soldier)
    print(f"Eliminated soldier: {el_sol} (Remaining: {soldier})")

print(f"The sole survivor is: {soldier}")