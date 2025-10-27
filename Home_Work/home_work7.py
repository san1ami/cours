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
        ("451° по Фаренгейту", "Рэй Брэдбери", 1953, "Антиутопия", 249, 5),
        ("Тень горы", "Грегори Дэвид Робертс", 2015, "Приключенческий роман", 864, 3),
        ("Имя розы", "Умберто Эко", 1980, "Детектив", 502, 2),
        ("Сто лет одиночества", "Габриэль Гарсиа Маркес", 1967, "Магический реализм", 416, 4),
        ("Цветы для Элджернона", "Дэниел Киз", 1959, "Фантастика", 320, 6),
        ("Американские боги", "Нил Гейман", 2001, "Фэнтези", 592, 4),
        ("Алхимик", "Пауло Коэльо", 1988, "Философская притча", 224, 5),
        ("Бойцовский клуб", "Чак Паланик", 1996, "Роман", 218, 3),
        ("Дюна", "Фрэнк Герберт", 1965, "Научная фантастика", 688, 7),
        ("Мёртвые души", "Николай Гоголь", 1842, "Сатира", 352, 2)
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
