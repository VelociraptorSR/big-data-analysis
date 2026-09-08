books = [

]

id_counter = len(books)

def add_book():
    global id_counter
    try:
        print("----------Add Book----------")
        title = input("Enter the title of the book: ").strip()
        if title == "":
            print("Title cannot be empty. Please try again. ")
            return
        author = input("Enter the author of the book: ").strip()
        if author == "":
            print("Author name cannot be empty. Please try again. ")
            return
        genre = input("Enter the genre of the book: ").strip()
        if genre == "":
            print("Genre cannot be empty. Please try again. ")
            return
        price = float(input("Enter the price of the book: "))
        if price <= 0:
            print("Price should be greater than zero. Please try again. ")
            return
        copies = int(input("Enter the copies of the book: "))
        if copies < 0:
            print("Copies cannot be less than zero. Please try again. ")
            return
        books.append({"ID" : id_counter+1, "Book Title" : title, "Author Name" : author, "Genre" : genre, "Price" : price, "Copies" : copies})
        id_counter += 1
    except ValueError:
        print("Please try with correct value. ")
        
def view_catalog():
    if len(books) == 0:
        print("No books in the library. ")
        return
    if len(books)  == 1:
        view_one(books)
    else:
        view_many(books)

def view_one(books):
    print("_"*40) 
    print(f"ID             :    {books[0]["ID"]}")   
    print(f"Book Title     :    {books[0]["Book Title"]}")   
    print(f"Author Name    :    {books[0]["Author Name"]}")   
    print(f"Genre          :    {books[0]["Genre"]}")   
    print(f"Price          :    {books[0]["Price"]}")   
    print(f"Copies         :    {books[0]["Copies"]}")   
    print("_"*40)    

def view_many(books):
    print("-"*80)
    print(f"{'ID':^5}{'Book Title':<20}{'Author Name':<20}{'Genre':<15}{'Price':>10}{'Copies':>10}")
    print("-"*80)
    for d in books:
        bid, title, author, genre, price, copies = d.values()
        print(f"{bid:^5}{title:<20}{author:<20}{genre:<15}{price:>10.2f}{copies:>10}")
    print("-"*80)
    
def search_book():
    try:
        print("1. Search by ID. ")
        print("2. Search by Title. ")
        print("3. Search by Author. ")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                search_by_id()
            case 2:
                search_by_title()
            case 3:
                search_by_author()
            case _:
                print("Invalid choice. Please retry. ")
    except:
        print("Please try with integer value. ")

def search_by_id():
    try:
        bid = int(input("Enter id of the book: "))
        result = [d for d in books if d["ID"] == bid ]
        if not result:
            print(f"No book found with id = {bid}")
            return
        view_one(result)
        return result
    except ValueError:
        print("Please try with integer vlaue. ")   

def search_by_title():
    title = input("Enter title of the book: ").lower()
    result = [d for d in books if d["Book Title"].lower() == title ]
    if not result:
        print(f"No book found with Book Tilte = {title}")
        return
    if len(result) == 1:
        view_one(result)
    else:
        view_many(result)

def search_by_author():
    author = input("Enter author of the book: ").lower()
    result = [d for d in books if d["Author Name"].lower() == author ]
    if not result:
        print(f"No book found with Author Name = {author}")
        return
    if len(result) == 1:
        view_one(result)
    else:
        view_many(result) 
        
def update_details():
    result = search_by_id() 
    if not result:
        return
    else:
        try:
            price = float(input("Enter the new price: "))
            if price <= 0:
                print("Price should be greater than zero please try again.")
                return
            copy = int(input("Enter number of copies: "))
            if copy < 0:
                print("Number of Copies should be grater than zero. ")
                return
            result[0]["Price"] = price
            result[0]["Copies"] = copy
        except ValueError:
            print("Please try with integer. ")
            
        
def delete_book():
    result = search_by_id()
    if not result:
        return
    else:
        yn = input("Do you want to delete the record (y/n): ").strip().lower()
        if yn == "y":
            books.remove(result[0])
            print("Record deleted successfully. ")
            return  

def save_to_file():
    global books
    with open("data.txt", mode = "w") as file:
        for d in books:
            file.writelines(f"{d['ID']}|{d['Book Title']}|{d['Author Name']}|{d['Genre']}|{str(d['Price'])}|{str(d['Copies'])}\n")
    print("Data saved successfully. ")

def load_form_file():
    global books
    try:
        with open("data.txt", mode = "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                bid, book_title, author, genre, price, copies = line.split("|")
                books.append({"ID" : int(bid), "Book Title" : book_title, "Author Name" : author, "Genre" : genre, "Price" : float(price), "Copies" : int(copies)})
        print("Data load successfully. ")
    except FileNotFoundError:
        print("File not found. ")

def menu():
    main_menu = '''    1. Add Book
    2. View Catalog
    3. Search Book
    4. Update Details
    5. Delete Book
    6. Save To File
    7. Load From File
    8. Exit
    '''
    print("--------Book Management System--------")
    print(main_menu)
    try:
        choice = int(input("Enter your choice: "))
    except:
        choice = -1
    return choice

def main():
    load_form_file()
    while True:
        choice = menu()
        match choice:
            case 1:
                add_book()
            case 2:
                view_catalog()
            case 3:
                search_book()
            case 4:
                update_details()
            case 5:
                delete_book()
            case 6:
                save_to_file()
            case 7:
                load_form_file()
            case 8:
                break
            case _:
                print("Invalid choice. Please try again. ")
        
        
        

if __name__ == "__main__":
    main()