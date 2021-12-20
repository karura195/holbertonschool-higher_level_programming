#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    curs = db.cursor()
    sql = """SELECT cities.id, cities.name, states.name
          FROM cities INNER JOIN states
          ON cities.state_id = states.id ORDER by id ASC"""
    curs.execute(sql)
    data = curs.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()
