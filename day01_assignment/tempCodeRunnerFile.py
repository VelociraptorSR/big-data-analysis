    inventory = {"Python Basics": 10, "Learning AI": 5}
    book_title = input("enter the title of book: ")
    quantity = input("enter the quantity of books: ")
    action = input("enter the action that you want to do (sell, add, lookup): ")
    print(type(quantity))
    print(type(inventory[book_title]))
    print(inventory[book_title])