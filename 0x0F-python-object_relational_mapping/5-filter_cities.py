#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa  """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""
                    SELECT cities.name
                    FROM cities
                    INNER JOIN states on states.id=cities.state_id
                    WHERE states.name=%s""", (sys.argv[4],))
    state = cur.fetchall()
    tmp = list(city[0] for city in state)
    print(*tmp, sep=", ")

    cur.close()
    db.close()