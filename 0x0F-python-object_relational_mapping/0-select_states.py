#!/usr/bin/python3
""" our script should take 3 arguments: mysql username, mysql password and
database name (no argument validation needed)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
