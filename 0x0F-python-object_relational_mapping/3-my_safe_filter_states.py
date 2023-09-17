#!/usr/bin/python3

"""A script that takes in arguments
and displays all values in the states table"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    state_name = sys.argv[4]
    cur.execute(query, (state_name,))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
