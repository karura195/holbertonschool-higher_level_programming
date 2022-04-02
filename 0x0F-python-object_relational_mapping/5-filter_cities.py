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
    sql = "SELECT cities.name "
    sql += "FROM cities JOIN states "
    sql += "ON cities.state_id = states.id "
    sql += "WHERE states.name = '{state}' ORDER by cities.id ASC"
    cur.execute(sql.format(state))
    query_rows = cur.fetchall()

    print(", ".join(row[0] for row in query_rows))
    cur.close()
    db.close()
