from typing import List, Dict, Callable

def add_book() -> None:
    title: str = input("Title: ").strip().title()
    author: str = input("Author: ").strip().title()
    year: str = input("Year of publication: ").strip()

    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year},Not Read\n")

def delete_book(books: List[Dict[str, str]], book_to_delete: Dict[str, str]) -> None:
    books.remove(book_to_delete)

def find_books() -> List[Dict[str, str]]:
    reading_list: List[Dict[str, str]] = get_all_books()
    matching_books: List[Dict[str, str]] = []

    search_term: str = input("Please enter a book title: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books

def get_all_books() -> List[Dict[str, str]]:
    books: List[Dict[str, str]] = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year, read_status = book.strip().split(",")

            books.append({
                "title": title,
                "author": author,
                "year": year,
                "read": read_status
            })

    return books

def mark_book_as_read(books: List[Dict[str, str]], book_to_update: Dict[str, str]) -> None:
    index: int = books.index(book_to_update)
    books[index]['read'] = "Read"

def update_reading_list(operation: Callable[[List[Dict[str, str]], Dict[str, str]], None]) -> None:
    books: List[Dict[str, str]] = get_all_books()
    matching_books: List[Dict[str, str]] = find_books()

    if matching_books:
        operation(books, matching_books[0])

        with open("books.csv", "w") as reading_list:
            for book in books:
                reading_list.write(",".join(book.values()) + "\n")
    else:
        print("Sorry, we didn't find any books matching that title.")

def show_books(books: List[Dict[str, str]]) -> None:
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']}) - {book['read']}")

    print()

menu_prompt: str = """Please enter one of the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

selected_option: str = input(menu_prompt).strip().lower()

while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "d":
        update_reading_list(delete_book)
    elif selected_option == "l":
        reading_list: List[Dict[str, str]] = get_all_books()

        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selected_option == "r":
        update_reading_list(mark_book_as_read)
    elif selected_option == "s":
        matching_books: List[Dict[str, str]] = find_books()

        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    selected_option = input(menu_prompt).strip().lower()

