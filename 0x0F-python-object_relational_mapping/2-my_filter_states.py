import sys 
import MySQLdb

if 'name' == 'main' :
    db = MySQL.connect(user = sys.argv[1] , passwd = sys.argv[2]  , db = sys.argv[3])
    cursor = db.cursor()
    cursor.execute(SELECT * FROM 'states' ORDERED BY 'id')
    [print 
