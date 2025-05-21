import sqlite3
from models.book import Book

class BookRepository:
    def __init__(self, db_name="books.db"):
        self.db_name = db_name

    def add_book(self, book: Book):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO books (id, title, author, year)
                VALUES (?, ?, ?, ?)
            """, (book.id, book.title, book.author, book.year))
            conn.commit()

    def get_book_by_id(self, book_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
            row = cursor.fetchone()
            if row:
                return Book(id=row[0], title=row[1], author=row[2], year=row[3])
            return None

    def update_book(self, book: Book):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE books
                SET title = ?, author = ?, year = ?
                WHERE id = ?
            """, (book.title, book.author, book.year, book.id))
            conn.commit()
            # Return True if any row was updated, False otherwise
            return cursor.rowcount > 0

    def delete_book(self, book_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()
            # Return True if any row was deleted, False otherwise
            return cursor.rowcount > 0

    def list_all_books(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            books = []
            for row in rows:
                books.append(Book(id=row[0], title=row[1], author=row[2], year=row[3]))
            return books

from models.book import Book
from services.book_service import BookRepository

class BookService:
    def __init__(self):
        self.book_repository = BookRepository()

    def add_book(self, book: Book):
        # You might want to add validation here if needed
        self.book_repository.add_book(book)

    def get_book_by_id(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            return None
        return self.book_repository.get_book_by_id(book_id)

    def update_book(self, book: Book):
        # Before update, check if book exists
        existing_book = self.get_book_by_id(book.id)
        if not existing_book:
            return False
        # Call update and return the boolean result from repository
        return self.book_repository.update_book(book)

    def delete_book(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            return False
        # Check if book exists
        existing_book = self.get_book_by_id(book_id)
        if not existing_book:
            return False
        # Call delete and return boolean result from repository
        return self.book_repository.delete_book(book_id)

    def list_all_books(self):
        return self.book_repository.list_all_books()
