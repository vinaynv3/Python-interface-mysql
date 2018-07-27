import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    global conn
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='Lonewolf1###')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()
        print('.....!!!!!!!........')
        print('Connection Closed')


if __name__ == '__main__':
    connect()