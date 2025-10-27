import sqlite3


def create_connection():
    return sqlite3.connect("../library.db")


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        );
    """)

    conn.commit()
    conn.close()
    print("Таблица успешно создана!")


def insert_books():
    conn = create_connection()
    cursor = conn.cursor()

    books_data = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 3),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Drama", 281, 4),
        ("Brave New World", "Aldous Huxley", 1932, "Science Fiction", 311, 6),
        ("Moby Dick", "Herman Melville", 1851, "Adventure", 635, 2),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 3),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Drama", 671, 4),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 223, 10),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 7),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Novel", 277, 4)
    ]

    cursor.executemany("""
        INSERT INTO books
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books_data)

    conn.commit()
    conn.close()
    print("Книги успешно добавлены!")


def delete_book(book_name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE name = ?", (book_name,))
    conn.commit()
    conn.close()
    print(f"Книга '{book_name}' удалена!")


if __name__ == "__main__":
    create_table()
    insert_books()
    delete_book("1984")
