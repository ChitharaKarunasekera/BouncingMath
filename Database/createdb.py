import mysql.connector

def bdexist():
    "This function is to check the existance of the database"
    global mycursor 
    db = []
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd=""
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for dbs in mycursor:
        for database in dbs:
            db.append(database)

    if 'bouncing_math' in db:
        ex = 1
    else:
        ex = 0

    return ex

def tblexist():
    "This function is to check the existance of the table"
    global mycursor
    tb = []
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="bouncing_math"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for tbls in mycursor:
        for table in tbls:
            tb.append(table)

    if 'gameinfo' in tb:
        extbl = 1
    else:
        extbl = 0
    return extbl

def createdb():
    "This function is to create a database"

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd=""
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE bouncing_math")
    return

def createtbl():
    "This funcrion in sto create a table in the database"

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="bouncing_math"
    )

    mycursor = mydb.cursor()
    
    playerTbl = ("CREATE TABLE gameinfo (rcdNo int NOT NULL AUTO_INCREMENT,name VARCHAR(7),correct INT(5),totQues INT(5),percentage INT(5),Level VARCHAR(6),Time TIME,Date DATE,PRIMARY KEY (rcdNo))")
    
    mycursor.execute(playerTbl)
    return

def alttbl():
    "This funcrion in sto create a table in the database"

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="bouncing_math"
    )

    mycursor = mydb.cursor()
    
    mycursor.execute("ALTER TABLE gameinfo AUTO_INCREMENT=100;")
    
    return

