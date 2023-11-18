#!/usr/bin/python3
'''Script to get all states'''
import MySQLdb
import sys


def list_states(username, password, database):
    '''Connect to the MySQL server and fetch records'''
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    query = 'SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id'
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)
