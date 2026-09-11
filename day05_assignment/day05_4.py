'''
Dynamic Data Pipeline with Lambdas & Custom Sorting
Scenario
An AI classification pipeline processes raw data inputs. Each raw input is a tuple of string annotations describing a product name, its price, and rating. 
The pipeline needs to clean, filter, and sort these records.

Problem Description
Write a function process_dataset(dataset) that processes a dataset using built-in higher-order functions (map, filter) and lambda expressions:

dataset is a list of tuples containing string records. Example:
[("Laptop", "Price: 1200", "Rating: 4.8"), ("Phone", "Price: 800", "Rating: 4.5")]
Your pipeline must execute the following sequential steps:
Parsing: From the incoming raw tuples, extract the product name (string), numeric price (float), and rating (float). (You can use string splitting or 
RegEx to isolate the numeric values).
Filtering: Use filter() with a lambda function to keep only items with a parsed price less than or equal to 1000.0.
Mapping: Use map() with a lambda function to transform the filtered entries into dictionaries of the following structure: 
{"product": <name>, "price": <float_price>, "score": <float_rating>}.
Sorting: Sort the resulting list of dictionaries in descending order of their score using sorted() with a lambda key selector. 
If two items have the same score, their relative order does not matter.
The function should return the sorted list of dictionaries.
Sample Input
data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]
Expected Output
[
    {"product": "Mouse", "price": 25.0, "score": 4.7},
    {"product": "Phone", "price": 800.0, "score": 4.5},
    {"product": "Charger", "price": 15.0, "score": 4.2}
]
(Note: "Laptop" is excluded since its price of 1200 exceeds 1000.0).
'''
import os

def process_dataset(dataset):
    expect_out = []
    for list_item in dataset:
        # dict = {}
        expect_out.append({    "product" : list_item[0], 
                               "price" : float(list_item[1].split(" ")[1]), 
                               "score" : float(list_item[2].split(" ")[1])
                            }
                        )
    #  new_result = list(filter(lambda x: x is not  "", new_result))
            
    expect_out = list(filter(lambda x:x["price"]<=1000 , expect_out))
    
    return expect_out

def main():
    data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
    ]
    result = process_dataset(data_input)
    print(result)

if __name__ == "__main__":
    os.system("cls")
    main()