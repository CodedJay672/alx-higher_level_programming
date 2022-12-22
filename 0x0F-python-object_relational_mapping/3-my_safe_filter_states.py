#!/usr/bin/python3

"""
   python script which searches for a name
   in the states table.
   The name of the state to search will be taken as
   argument from the command line
   script implements MySQLdb library

"""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(
            host="localhost",
            user=args[1],
            passwd=args[2],
            db=args[3],
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
                WHERE states.name = '%s'\
                ORDER BY states.id ASC;" % (sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
