#!/usr/bin/python3
""" takes in arguments and displays all values in the states table
    where name matches the argument and is safe from MySQL injections """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    curs = db.cursor()
    name = argv[4]
    sql = "SELECT * FROM states WHERE name COLLATE utf8mb4_bin = %s "
    sql += "ORDER BY id ASC"
    curs.execute(sql, (name, ))
    data = curs.fetchall()
    for row in data:
        print(row)
    curs.close()
    db.close()
