from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def insert_books(books):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, books)
        print('Books details successfully inserted into table')

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()


def main():
    books = [('old man in the sea', '9780439354571'),
             ('kite runner', '9781146675536'),
             ('Alchemist', '9780679785668')]
    insert_books(books)


if __name__ == '__main__':
    main()