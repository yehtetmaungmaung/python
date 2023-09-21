"""
Complete the following with required statements.
#import required module for connecting database
________(1)______

# Open database connection
db = ____(2)_____(host="127.0.0.1", port=3306,
 user="root", passwd="", db="testdb")

# prepare a cursor object 
cursor = ____(3)____

# Prepare SQL query to INSERT a record into the database.
sql = INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # Execute the SQL command
   ______(4)_______
   # Commit your changes in the database
   db.commit( )
except:
   # Rollback in case there is any error
   db.rollback( )

# disconnect from server
   ______(5)_______
"""

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    passwd="",
    db="testdb"
)

cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    print(e)

db.close()