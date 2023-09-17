#!/usr/bin/python3

"""  lists all states from the database hbtn_0e_0_usa """
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
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()
    if states:
        for state in states:
            print(state)
    else:
        print("No matching state found")

    cur.close()
    db.close()
