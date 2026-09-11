'''
    Atomic E-Commerce Order Processor
    Scenario
    You are building an ordering subsystem for an online store. Orders containing multiple products must be processed 
    atomically: either the entire order completes successfully, or the entire transaction fails. If one item in the order 
    is out of stock or is unrecognized, no stock should be deducted for any other item (rollback).

    Problem Description
    Define two custom exceptions:
    ProductNotFoundError (raised when a product ID is not present in the catalog).
    OutOfStockError (raised when the customer's ordered quantity exceeds the available stock).
    Write a function process_order(catalog, order):
    catalog is a dictionary containing product database records. Format:
    catalog = {
        "P01": {"price": 100.0, "stock": 5},
        "P02": {"price": 50.0, "stock": 2}
    }
    order is a dictionary containing product IDs (keys) and quantities ordered (values). Format: {"P01": 2, "P02": 1}.
    Validation Phase: Before modifying any inventory levels:
    Check if all ordered keys exist in the catalog. If a product ID does not exist, raise ProductNotFoundError with message: 
    "Product '<product_id>' not found in store catalog."
    Check if the catalog contains sufficient stock for each item ordered. If the ordered quantity exceeds available stock, 
    raise OutOfStockError with message: "Product '<product_id>' is out of stock. Requested: <requested_qty>, Available: 
    <available_stock>."
    Execution Phase: If (and only if) all products pass validation:
    Deduct the ordered quantities from the stock numbers in the catalog dictionary.
    Calculate and return the total cost of the order (float).
    If an exception was raised during validation, the catalog must remain completely unchanged.
    Example Walkthrough
    catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }

    # 1. Successful Order
    total = process_order(catalog, {"P01": 2, "P02": 1})
    # Returns: 40.0
    # Catalog stock changes to: P01 stock = 3, P02 stock = 9

    # 2. Failed Order (Triggers Rollback)
    # Current Catalog: {"P01": {"price": 10.0, "stock": 3}, "P02": {"price": 20.0, "stock": 9}}
    try:
        total = process_order(catalog, {"P01": 2, "P02": 15})
    except OutOfStockError as e:
        print(e) # Output: Product 'P02' is out of stock. Requested: 15, Available: 9.

    # Verify Catalog Stock: P01 must remain at 3 (NOT decreased to 1).
    print(catalog["P01"]["stock"]) # Output: 3
'''

import os

class ProductNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

def process_order(catalog, order):
    # -------- VALIDATION PHASE --------
    for product_id, quantity in order.items():
        # Check whether product exists
        if product_id not in catalog:
            raise ProductNotFoundError(
                f"Product '{product_id}' not found in store catalog."
            )
        
        # Check whether enough stock exists
        available_stock = catalog[product_id]["stock"]
        if quantity > available_stock:
            raise OutOfStockError(
                f"Product '{product_id}' is out of stock. "
                f"Requested: {quantity}, Available: {available_stock}."
            )
            
    total_price = 0.0
    for product_id, quantity in order.items():
        product = catalog[product_id]
        product["stock"] -= quantity
        total_price += product["price"] * quantity
        
    return total_price

def main():
    # Initial state
    catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }
    
    # 1. Successful Order Case
    print("Initial Catalog State:", catalog)
    try:
        order1 = {"P01": 2, "P02": 2}
        total = process_order(catalog, order1)
        print(f"Order Successful! Total Cost: {total}")
        print("Catalog after successful order:", catalog)
    except (ProductNotFoundError, OutOfStockError) as e:
        print(e)
    print()
    
    # 2. Out Of Stock Case (Triggers Rollback Verification)
    try:
        order2 = {"P01": 1, "P02": 15}
        total = process_order(catalog, order2)
        print(f"Order Successful! Total Cost: {total}")
    except (ProductNotFoundError, OutOfStockError) as e:
        print("Caught Expected Error:", e)
        print("Catalog after rollback (Stock must remain unchanged):", catalog)
    print()

    # 3. Product Not Found Case
    try:
        order3 = {"P03": 1}
        total = process_order(catalog, order3)
        print(f"Order Successful! Total Cost: {total}")
    except (ProductNotFoundError, OutOfStockError) as e:
        print("Caught Expected Error:", e)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Atomic E-Commerce Order Processor ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)
