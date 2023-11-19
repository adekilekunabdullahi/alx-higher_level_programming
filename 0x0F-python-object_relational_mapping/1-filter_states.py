#!/usr/bin/python3
"""Filter states"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    query = 'SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id'
    cursorDb = connection.cursor()
    cursorDb.execute(query)
    for row in cursorDb.fetchall():
        print(row)
    cursorDb.close()
    connection.close()
