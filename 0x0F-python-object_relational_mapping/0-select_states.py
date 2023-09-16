import MySQLdb
import sys


if len(sys.argv) != 4:
    print("Usage: python 0-select_states.py
          < username > < password > < database_name >")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database_name, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id;")

    states = cur.fetchall()

    for state in states:
        print(state)

    db.close()
    cur.close()
