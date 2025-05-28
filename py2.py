import mysql.connector
from mysql.connector import Error
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imking51",
            database="book_db"
        )
        return conn
    except Error as e:
        print("Connection Error:", e)
        return None
def insert_book(conn, title, author, isbn, publication_year):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, isbn, publication_year) VALUES (%s, %s, %s, %s)",
            (title, author, isbn, publication_year)
        )
        conn.commit()
        print(f"Inserted: {title}")
    except Error as e:
        print("Insert Error:", e)

def get_book(conn, isbn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
        result = cursor.fetchone()
        return result
    except Error as e:
        print("Get Error:", e)
        return None

def update_book(conn, isbn, new_title, new_author, new_year):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE books 
            SET title = %s, author = %s, publication_year = %s 
            WHERE isbn = %s
        """, (new_title, new_author, new_year, isbn))
        conn.commit()
        print(f"Updated ISBN {isbn}")
    except Error as e:
        print("Update Error:", e)

def delete_book(conn, isbn):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE isbn = %s", (isbn,))
        conn.commit()
        print(f"Deleted ISBN {isbn}")
    except Error as e:
        print("Delete Error:", e)
def main():
    conn = create_connection()
    if conn is None:
        return
    insert_book(conn, "The Hobbit", "J.R.R. Tolkien", "9780007458424", 1937)
    insert_book(conn, "Pride and Prejudice", "Jane Austen", "9780141439518", 1813)
    insert_book(conn, "Moby Dick", "Herman Melville", "9781503280786", 1851)
    book = get_book(conn, "9780141439518")
    print("\nRetrieved Book:", book)

    update_book(conn, "9781503280786", "Moby-Dick", "H. Melville", 1851)
    updated = get_book(conn, "9781503280786")
    print("Updated Book:", updated)


    delete_book(conn, "9780007458424")
    deleted = get_book(conn, "9780007458424")
    print("After Deletion (should be None):", deleted)

    conn.close()

if __name__ == "__main__":
    main()
