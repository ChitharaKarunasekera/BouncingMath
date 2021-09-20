import mysql.connector
from prettytable import PrettyTable


def connect():
    "This function is to bulid connection with thw database"
    global conDict
    global db
    global cursor

    #Open database connection with a dictionery
    conDict = {'host':'localhost',
                'database':'bouncing_math',
                'user':'root',
                'password':''}

    db = mysql.connector.connect(**conDict)

    cursor = db.cursor()
    return

def insert(name,num,score,perc,lev,time,date):
    "Function to insert values to the database"

    #SQL query
    mySQLText = "INSERT INTO gameinfo(name, correct, totQues,percentage, Level, Time, Date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    myValues = (name, score, num, perc,lev,time,date)
    cursor.execute(mySQLText, myValues)

    db.commit()

    db.close()
    return

def allInfo():
    "Function to display information of all players"
    tbl = PrettyTable()
    tbl.field_names = ["Name", "Corrct answers", "Total questions", "Percentage"]

    #Execute SQL query 
    cursor.execute("SELECT name, correct, totQues, percentage  FROM gameinfo")

    data = cursor.fetchall()

    for item in data:
        tbl.add_row(item)
        
    print("Past player results")
    print(tbl)

    db.close()
    return

def user():
    user = []
    global uName
    
    #Get record name of user
    uName = input("Enter user name: ")

    #Execute SQL query using execute() method
    cursor.execute("SELECT name FROM gameinfo")

    data = cursor.fetchall()

    for item in data:
        for nameitem in item:
            user.append(nameitem)

    if uName in user:
        use = 1
        
    else:
        use = 0
        
    db.close()
    return use

def userinfo():
    uName = input("Enter user name: ")
    
    tbl = PrettyTable()
    tbl.field_names = ["Record No.", "Name", "Corrct answers", "No. of questions", "Percentage","Level","Time","Date"]
    
    
    #Execute SQL query 
    shwTxt= "SELECT * FROM gameinfo WHERE name = %s"
    getTxt = (uName,)
    
    cursor.execute(shwTxt,getTxt)

    data = cursor.fetchall()

    for item in data:
        tbl.add_row(item)
        
    print("Information of user")
    print(tbl)
    print("Total number of records: ",cursor.rowcount)

    db.close()
    return


def method():
    global m
    print("----Past game infromation method----")
    print("1 - All game records")
    print("2 - Player's game infromation")
    print("\n")

    methd = input("Select records viewing method: ")

    if(methd == "2"):
        userinfo()
        delete()
    elif(methd == "1"):
        allInfo()
    else:
        print("Invalied option")
    return


def delete():
    connect()
    while True:
        delt = input("Do you want to delete a record (Y\\N)?")
        if (delt == "y" or delt == "Y" ):
            try: 
                delrcd = input("Enter record number: ")
                cursor = db.cursor()

                cursor.execute("DELETE FROM gameinfo WHERE rcdNo =" + delrcd + "")

                db.commit()
                
                print(cursor.rowcount, "Record", delrcd, "Deleted")

                db.close()
            except:
                print("Invalied Record number!")
        elif(delt == "n" or delt == "N"):
            break



