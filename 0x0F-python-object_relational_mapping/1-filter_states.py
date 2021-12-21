#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    curs = db.cursor()
    sql = "SELECT * FROM states WHERE name COLLATE utf8mb4_bin "
    sql += "LIKE 'N%' ORDER BY states.id ASC"
    curs.execute(sql)
    data = curs.fetchall()
    for row in data:
        print(row)
    curs.close()
    db.close()
