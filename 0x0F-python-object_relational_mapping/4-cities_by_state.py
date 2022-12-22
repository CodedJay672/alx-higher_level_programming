#!/usr/bin/python3

"""
   Python script that lists all cities in a database
   the script takes 3 args: u.name, passwd and database
   script implements the MySQLdb module

"""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(host='localhost',
                           user=args[1],
                           passwd=args[2],
                           db=args[3])
    cur = conn.cursor()

    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c\
                JOIN states AS s ON c.state_id = s.id\
                ORDER BY c.id ASC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)
