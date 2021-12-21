#!/usr/bin/python3
""" takes in an argument and displays all values in the states table """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name COLLATE utf8mb4_bin = '{}' "
    sql += "ORDER BY id ASC"
    cursor.execute(sql.format(argv[4]))
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
