#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    curs = db.cursor()
    name = argv[4]
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    curs.execute(sql, (name, ))
    data = curs.fetchall()
    for row in data:
        print(row)
    curs.close()
    db.close()
