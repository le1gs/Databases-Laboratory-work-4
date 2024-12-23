
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['library']
books_collection = db['books']

def create_book(title, author, genre, year):
    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year
    }
    books_collection.insert_one(book)
    print(f"Book '{title}' added successfully!")

def read_books():
    books = books_collection.find()
    for book in books:
        print(f"ID: {book['_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Year: {book['year']}")

def update_book(book_id, title=None, author=None, genre=None, year=None):
    updates = {}
    if title: updates["title"] = title
    if author: updates["author"] = author
    if genre: updates["genre"] = genre
    if year: updates["year"] = year
    result = books_collection.update_one({"_id": book_id}, {"$set": updates})
    if result.modified_count > 0:
        print("Book updated successfully!")
    else:
        print("No changes were made.")

def delete_book(book_id):
    result = books_collection.delete_one({"_id": book_id})
    if result.deleted_count > 0:
        print("Book deleted successfully!")
    else:
        print("Book not found.")

def main():
    while True:
        print("\nChoose an action:")
        print("1. Add a book")
        print("2. View all books")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            year = int(input("Enter year of publication: "))
            create_book(title, author, genre, year)
        elif choice == "2":
            read_books()
        elif choice == "3":
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title (leave blank to skip): ")
            author = input("Enter new author (leave blank to skip): ")
            genre = input("Enter new genre (leave blank to skip): ")
            year = input("Enter new year (leave blank to skip): ")
            year = int(year) if year else None
            update_book(book_id, title, author, genre, year)
        elif choice == "4":
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
