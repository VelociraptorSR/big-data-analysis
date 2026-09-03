#  https://cf.cdacb.in/index.php/s/T0esq2yzIfC22wl

# class Person:

#     def __init__(self, **kwargs):
#         self.name = kwargs.get('name')
#         self.city = kwargs.get('city')


# class Employee(Person):

#     def __init__(self, **kwargs):
#         # invoke parent class __init__
#         super().__init__(**kwargs)

#         self.department = kwargs.get('department')
#         self.salary = kwargs.get('salary')


# p1 = Person(name='Ramesh', city='Chennai')

# # e1 = Employee(
# #     name='Suresh',
# #     city='Jaipur',
# #     department='ADMIN',
# #     salary=55000
# # )

# print(p1.__dict__)

class Error(Exception):
    pass


def manage_bookstore_inventory(inventory, action, book_title, quantity=0):
    if action == "sell":
        if book_title not in inventory.keys():
            raise Error(f"Book '{book_title}' not found in inventory.")
        if quantity > inventory[book_title]:
            raise Error(f"Insufficient stock for '{book_title}'. Available: {inventory[book_title]}.")
        
    if action == "add":
        if book_title not in inventory.keys():
            inventory[book_title] = quantity
        else:
            inventory[book_title] = inventory[book_title] + quantity
    
    if action == "sell":
        pass
    
try:
    inventory = {"Python Basics": 10, "Learning AI": 5}
    book_title = input("enter the title of book: ")
    quantity = input("enter the quantity of books: ")
    action = input("enter the action that you want to do (sell, add, lookup): ")
    print(type(quantity))
    print(type(inventory[book_title]))
    print(inventory[book_title])
    result = manage_bookstore_inventory(inventory, action, book_title, quantity)
    print(f"Result: {result}")
    
except Error as e:
    print(e)
    
    
    