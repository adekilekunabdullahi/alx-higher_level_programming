#!/usr/bin/python3
"""All cities by state"""
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
    cursr = connection.cursor()
    citiesQuery = 'SELECT cities.name FROM cities JOIN states ON \
        cities.state_id=states.id WHERE states.name LIKE %s ORDER \
            BY cities.id'
    cursr.execute(citiesQuery, (argv[4],))
    print(', '.join(cty[0] for cty in cursr.fetchall()))
    cursr.close()
    connection.close()
