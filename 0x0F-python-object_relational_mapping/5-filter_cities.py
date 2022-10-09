#!/usr/bin/python3
"""
 script that takes in the name of a state as an argument and
 lists all cities of that state, using the database hbtn_0e_4_usa

 Your script should take 4 arguments: mysql username, mysql password,
 database name and state name (SQL injection free!)
 You must use the module MySQLdb (import MySQLdb)
 Your script should connect to a MySQL server running on localhost at port 3306
 Results must be sorted in ascending order by cities.id
 You can use only execute() once
 The results must be displayed as they are in the example below
 Your code should not be executed when imported
 """

import MySQLdb
from sys import argv, stdout

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    av = argv[4]
    if (av.__contains__('TRUNCATE' or 'FROM' or 'SELECT')):
        av = ''
    cur.execute('SELECT cities.name FROM cities INNER JOIN states\
                ON states.id=cities.state_id WHERE states.name= %s\
                ORDER BY cities.id', (av, ))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        for city in row:
            cities.append(city)
    if len(cities) != 0:
        for city in range(len(cities)):
            if city < len(cities) - 1:
                print(cities[city], end=', ')
        print(cities[city])
    cur.close()
    db.close()
