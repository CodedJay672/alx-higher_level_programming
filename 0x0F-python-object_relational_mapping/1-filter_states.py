#!/usr/bin/python3

"""
   Python script that lists all states with a name
   starting with the letter N (capital N).
   Result must be ordered by states.id in ascending
   order.

"""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(
            host='localhost',
            user=args[1],
            passwd=args[2],
            db=args[3]
            )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("(%s, '%s')" % (row[0], row[1]))
