#!/usr/bin/python3
"""Prevent SQL injection"""
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
    cursorDb = connection.cursor()
    cursorDb.execute('SELECT * FROM states WHERE name LIKE \
                     BINARY %(name)s ORDER BY id', {'name': argv[4]})
    for row in cursorDb.fetchall():
        print(row)
    cursorDb.close()
    connection.close()
