class Book:

    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute (by convention), default to False (available)

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """
        Marks the book as available if it's currently checked out.
        Returns True if successful, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Not checked out

    def is_available(self):
        """
        Checks if the book is currently available (not checked out).
        Returns True if available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        This is useful for debugging but not directly used by list_available_books
        to match the exact output format.
        """
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} ({status})"


class Library:
   
    def __init__(self):
       
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        if not isinstance(book, Book):
            print(f"Error: Cannot add '{book}'. Only Book objects can be added.")
            return

        # Check for duplicates
        for existing_book in self._books:
            if existing_book.title == book.title and existing_book.author == book.author:
                print(f"Book '{book.title}' by {book.author} already exists in the library.")
                return

        self._books.append(book)
        # This print is for robustness, not in expected output
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.
        Updates the book's _is_checked_out status.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()  # Delegate to the Book object's method
        return False  # Book not found

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()  # Delegate to the Book object's method
        return False  # Book not found

    def list_available_books(self):
        available_books_found = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_books_found = True
        
        if not available_books_found:
            print("No books currently available in the library.")
