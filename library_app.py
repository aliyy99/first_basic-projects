import json
import os

file = "library.json"

# Dosya yoksa oluştur
if not os.path.exists(file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=3)

def read_book():
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_book(books):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=3)
    
def add_book():
    name = input("Enter book name: ")
    writer = input("Enter book writer: ")
    year = int(input("Enter year of book: "))
    situation = "suitable"
    
    new_book = {
        "name": name,
        "writer": writer,
        "year": year,
        "situation": situation
    }
    
    books = read_book()
    books.append(new_book) 
    save_book(books)
    
    print(f"\n✓ '{name}' has been added successfully!\n")
    
def show_book():
    books = read_book()
    if not books:
        print("\nNo books found in library.\n")
    else:
        print("\n=== ALL BOOKS ===")
        for i, item in enumerate(books, 1):
            print(f"{i}. Name: {item['name']}, Writer: {item['writer']}, Year: {item['year']}, Status: {item['situation']}")
        

def search_book():
    search_term = input("Enter book name to search: ").lower()
    books = read_book()
    found = False
    
    print("\n=== SEARCH RESULTS ===")
    for item in books:
        if search_term in item['name'].lower():
            print(f"Name: {item['name']}, Writer: {item['writer']}, Year: {item['year']}, Status: {item['situation']}")
            found = True
    
    if not found:
        print("No books found with that name.")
    

def borrow_book():
    book_name = input("Enter book name to borrow: ")
    books = read_book()
    found = False
    
    for item in books:
        if item['name'].lower() == book_name.lower():
            if item['situation'] == "suitable":
                item['situation'] = "borrowed"
                save_book(books)
                print(f"\n✓ You borrowed '{book_name}' successfully!\n")
                found = True
            else:
                print(f"\n✗ '{book_name}' is already borrowed.\n")
                found = True
            break
    
    if not found:
        print(f"\n✗ Book '{book_name}' not found in library.\n")

def deliver_book():
    book_name = input("Enter book name to return: ")
    books = read_book()
    found = False
    
    for item in books:
        if item['name'].lower() == book_name.lower():
            if item['situation'] == "borrowed":
                item['situation'] = "suitable"
                save_book(books)
                print(f"\n✓ You returned '{book_name}' successfully!\n")
                found = True
            else:
                print(f"\n✗ '{book_name}' was not borrowed.\n")
                found = True
            break
    
    if not found:
        print(f"\n✗ Book '{book_name}' not found in library.\n")

# Ana Program
while True:
    print("=" * 40)
    print("WELCOME TO LIBRARY APP")
    print("=" * 40)
    print("1. Add book")
    print("2. Show all books")
    print("3. Borrow book")
    print("4. Search book")
    print("5. Deliver book")
    print("6. Exit")
    print("=" * 40)
    
    try:
        choice = int(input("Please choose an option (1-6): "))
        
        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            borrow_book()
        elif choice == 4:
            search_book()
        elif choice == 5:
            deliver_book()
        elif choice == 6:
            print("\nThank you for using Library App. Goodbye!\n")
            break
        else:
            print("\n✗ Invalid option! Please choose between 1-6.\n")
    
    except ValueError:

        print("\n✗ Please enter a valid number!\n")
