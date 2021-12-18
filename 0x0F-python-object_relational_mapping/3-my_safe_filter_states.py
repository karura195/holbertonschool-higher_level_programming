#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    name = argv[4]
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (name,))
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
