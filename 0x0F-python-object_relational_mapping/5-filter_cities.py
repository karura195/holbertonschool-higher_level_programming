#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists
all cities of that state """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    state = argv[4]
    cur = db.cursor()
    sql = "SELECT a.id, a.name "
    sql += "FROM cities a JOIN states b "
    sql += "ON a.state_id = b.id "
    sql += "WHERE b.name COLLATE utf8mb4_bin = %s ORDER BY 1;"
    params = (state, )
    cur.execute(sql, params)
    query_rows = cur.fetchall()
    cities = []
    for row in query_rows:
        cities.append(row[1])
    print(", ".join(cities))
    cur.close()
    db.close()
