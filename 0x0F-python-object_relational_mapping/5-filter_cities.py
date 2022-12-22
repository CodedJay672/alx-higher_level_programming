#!/usr/bin/python3
"""
   python script that prints the cities in a particular state
   state is passed as an argument in the command line
   result sorted by cities.id
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

    cur.execute(("SELECT c.name FROM cities AS c WHERE c.state_id = (SELECT states.id FROM states WHERE states.name = '{}');".format(args[4])))
    rows = cur.fetchall()

    print(', '.join(row[0] for row in rows))
