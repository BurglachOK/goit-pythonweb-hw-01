from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


@dataclass
class Book:
    title: str
    author: str
    year: int


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logging.info("Book '%s' added to the library \n", book.title)

    def remove_book(self, title: str) -> bool:
        for book in self._books:
            if book.title.lower() == title.lower():
                self._books.remove(book)
                logging.info("Book '%s' removed from the library \n", title)
                return True

        logging.info("Book '%s' not found \n", title)
        return False

    def get_books(self) -> list[Book]:
        return self._books.copy()


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title=title, author=author, year=year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()

        if not books:
            logging.info("Library is empty \n")
            return
        print("Books in the library:")
        for book in books:
            logging.info(
                "Title: %s, Author: %s, Year: %s",
                book.title,
                book.author,
                book.year,
            )


def main() -> None:
    library: LibraryInterface = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year_input = input("Enter book year: ").strip()

                if not year_input.isdigit():
                    logging.info("Year must be a number, please try again.")
                    year_input = input("Enter book year: ").strip()

                manager.add_book(title, author, int(year_input))

            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)

            case "show":
                manager.show_books()

            case "exit":
                logging.info("Closing the library manager. Goodbye! \n")
                break

            case _:
                logging.info("Invalid command. Please try again. \n")


if __name__ == "__main__":
    main()