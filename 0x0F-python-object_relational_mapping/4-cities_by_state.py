#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    curs = db.cursor()
    sql = "SELECT ci.id, ci.name, st.name "
    sql += "FROM cities ci JOIN states st "
    sql += "ON ci.state_id = st.id ORDER by id ASC"
    curs.execute(sql)
    data = curs.fetchall()
    for row in data:
        print(row)
    curs.close()
    db.close()
