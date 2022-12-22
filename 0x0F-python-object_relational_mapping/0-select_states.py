#!/usr/bin/python3
"""Script that lists all states from a database"""

import sys, MySQLdb

args = sys.argv
conn = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2], db=args[3])
cur = conn.cursor()
cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
rows = cur.fetchall()
for row in rows:
    print("(%s, '%s')" %(row[0], row[1]))
