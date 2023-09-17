#!/usr/bin/python3

"""Python ORM"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = db.cursor()
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (state_name,))
    states = cur.fetchall()
    if states:
        for state in states:
            print(state)
    else:
        print("No matching state found")

    cur.close()
    db.close()
