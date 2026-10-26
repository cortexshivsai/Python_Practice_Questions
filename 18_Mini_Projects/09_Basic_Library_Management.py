# Dictionary: book ID -> book title
books = {
    101: "Python Basics",
    102: "Data Structures",
    103: "Machine Learning",
    104: "Artificial Intelligence"
}

# Set containing IDs of books currently borrowed
borrowed_books = set()

while True:
    print("\n=== Library Management ===")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        for book_id, title in books.items():
            if book_id in borrowed_books:
                status = "Borrowed"
            else:
                status = "Available"

            print(book_id, "-", title, "-", status)

    elif choice == "2":
        try:
            book_id = int(input("Enter book ID to borrow: "))

            if book_id not in books:
                print("Book does not exist.")
            elif book_id in borrowed_books:
                print("Book is already borrowed.")
            else:
                borrowed_books.add(book_id)
                print("Book borrowed successfully.")

        except ValueError:
            print("Enter a valid book ID.")

    elif choice == "3":
        try:
            book_id = int(input("Enter book ID to return: "))

            if book_id in borrowed_books:
                borrowed_books.remove(book_id)
                print("Book returned successfully.")
            else:
                print("This book is not currently borrowed.")

        except ValueError:
            print("Enter a valid book ID.")

    elif choice == "4":
        print("Thank you for visiting the library.")
        break

    else:
        print("Invalid choice.")