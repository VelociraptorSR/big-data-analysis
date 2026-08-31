'''
Snake Game Board Renderer
Scenario: Render a simple 2D text game board. Write a program that performs the following steps in sequence:

Creates a 5×5 grid filled with dots "." represented as a nested list.
Places a food item "F" at grid position [2, 3].
Prompts the user to enter coordinate inputs: a row and a col (integers between 0 and 4) for the snake's head.
Places the snake's head "S" at the user-supplied coordinate [row, col], overwriting the character at that position.
If the user-supplied coordinates are exactly [2, 3], print the message "Yum! The snake ate the food!" 
(the snake "S" will occupy index [2, 3] on the printed board, overwriting the "F").
Prints the grid neatly line-by-line (each row's elements separated by spaces).
Sample Input: (User inputs Row 0 and Column 3)
Sample Output:
. . . S .
. . . . .
. . . F .
. . . . .
. . . . .
Sample Input: (User inputs Row 2 and Column 3)
Sample Output:
. . . . .
. . . . .
. . . S .
. . . . .
. . . . .
Yum! The snake ate the food!
'''
while True:
    eat = False
    position = input("Enter the position of the snake ")
    row, col = [int(n) for n in position.split(",")]
    for i in range(5):
        line = ''
        curr_col = ''
        for j in range(5):
            if i == 2 and j == 3:
                if i == row and j == col:
                    line += ' S '
                    eat = True
                else:
                    line += ' F '
            else:
                if i == row and j == col:
                    line += ' S '
                else:
                    line += ' . '
                    
        print(line)
        if i == 5 and j == 5:
            break
         
    if eat:
        print('Yum! The snake ate the food!')
        break
    else:
        print("Snake is hungry")