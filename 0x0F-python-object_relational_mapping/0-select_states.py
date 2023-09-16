import MySQLdb
import sys


if len(sys.argv) != 4:
    print("Usage: python 0-select_states.py <username> <password> <database_name>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

try:
    db = MySQLdb.connect(host ="localhost", user="jotham333", passwd="jotham087", db="hbtn_0e_0_usa")
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id;")

    states = cur.fetchall()

    for state in states:
        print(state)

except MySQLdb.Error as e:
    print(f"Error: {e}")

finally:
    if 'db' in locals() and db is not None:
        db.close()

    if 'cur' in locals() and cur is not None:
        cur.close()
