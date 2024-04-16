#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa sorted in ascending order by
states.id
"""
import MySQLdb
import sys
def list_states(username , password , database):
  db = MySQLdb.connect(host="localhost",port=3306,user=username,passwd=password,db=database)
  cursor = db.cursor()
  cursor.execute("SELECT * FROM STATES ORDERED BY id ASC")
  cursor.execute()
  rows = cursor.fetchall()
  for row in rows :
     print (row)
  db.close()
if __name__ == '__main__' :
  username = sys.argv[1]
  password = sys.argv[2]
  database = sys.argv[3]
  
  list_states(username , paasword , database)
