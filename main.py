from services.book_service import BookService
from models.book import Book

book_service = BookService()

def main():
    while True:
        print("\n--- Book CRUD Menu ---")
        print("1. Add Book")
        print("2. View Book by ID")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. List All Books")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Add Book selected")
            try:
                book_id = int(input("Enter book ID (number): "))
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = int(input("Enter publication year: "))

                book = Book(id=book_id, title=title, author=author, year=year)
                book_service.add_book(book)
                print(f"✅ Book '{title}' added successfully!")
            except ValueError:
                print("Please enter valid numeric values for ID and year.")

        elif choice == "2":
            print("View Book selected")
            try:
                book_id = int(input("Enter book ID to view: "))
                book = book_service.get_book_by_id(book_id)
                if book:
                    print("\n📖 Book Found:")
                    print(f"ID: {book.id}")
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"Year: {book.year}")
                else:
                    print("❌ Book not found.")
            except ValueError:
                print("Please enter a valid numeric book ID.")

        elif choice == "3":
            print("Update Book selected")
            try:
                book_id = int(input("Enter book ID to update: "))
                title = input("Enter new title: ")
                author = input("Enter new author: ")
                year = int(input("Enter new publication year: "))

                book = Book(id=book_id, title=title, author=author, year=year)
                success = book_service.update_book(book)
                if success:
                    print(f"✅ Book ID {book_id} updated successfully!")
                else:
                    print("❌ Book not found.")
            except ValueError:
                print("Please enter valid numeric values for ID and year.")

        elif choice == "4":
            print("Delete Book selected")
            try:
                book_id = int(input("Enter book ID to delete: "))
                confirm = input(f"Are you sure you want to delete book ID {book_id}? (y/n): ").lower()
                if confirm == 'y':
                    success = book_service.delete_book(book_id)
                    if success:
                        print(f"✅ Book ID {book_id} deleted successfully!")
                    else:
                        print("❌ Book not found.")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Please enter a valid numeric book ID.")

        elif choice == "5":
            print("List All Books selected")
            books = book_service.list_all_books()
            if books:
                print("\n--- All Books ---")
                for book in books:
                    print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Year: {book.year}")
            else:
                print("No books found in the database.")

        elif choice == "6":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

