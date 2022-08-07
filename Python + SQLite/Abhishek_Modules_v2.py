# Date = 25 Nov 2021
# In Class Assignment 2 LO2
# COMP 1026
import sqlite3

def Abhishek_db_table_create():
    try:
        conn = sqlite3.connect('AbhishekDB.db')
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE AbhishekTABLE
            (enum integer, ename text, age integer, dept text, basicPay real,
            ta real,hra real,comm real,overtime real,grossPay real,ftax real,
            ptax real,cpa real,netPay real
        
            )''')
        conn.commit()
        print("Table created")
    except sqlite3.Error as error:
        print("Failed to read data from the database", error)
    finally:
        if (conn):
            c.close()
            print("The SQLite connection is closed")
            input("Press any key to go back to main menu ")


# Adding a new employee to organization database - option 2
def Abhishek_addEmployee():
    print("Enter the details of employee")
    print("-----------------------------")
    vEnum = int(input(" Enter employee Number: "))
    vEname = input(" Enter employee Name: ")
    vEage = int(input(" Enter employee age: "))
    vEdesig = input(" Enter Department (Enter any one of these(Sales,Mkt,Mgmt,Admin): ")
    vEbpay = float(input(" Enter employee Basic Pay: "))
    vEta = float(input("Enter the TA for the Employee: "))
    vEhra = float(input("Enter HRA for the Employee: "))
    vEcomm = float(input("Enter comm for the Employee: "))
    vEovertime = float(input("Enter overtime done by Employee: "))
    vEftax = float(input("Enter Federal Tax paid by the Employee: "))
    vEptax = float(input("Enter Provincial Tax paid by the Employee: "))
    vEcpa = float(input("Enter the Canada Pension Plan of the Employee: "))

    try:
        conn = sqlite3.connect('AbhishekDB.db')
        c = conn.cursor()

        # Insert a row of data
        c.execute("INSERT INTO AbhishekTABLE (enum,ename,age,dept,basicPay,ta,hra,comm,overtime,ftax,ptax,cpa) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(vEnum,vEname,vEage,vEdesig,vEbpay,vEta,vEhra,vEcomm,vEovertime,vEftax,vEptax,vEcpa,))
        # Save (commit) the changes
        conn.commit()
        print("Congratulations!! {0} , you are successfully added to Payroll register >>\n\n".format(vEname))
        input("Press enter to return back to Main Menu ")

    except sqlite3.Error as error:
        print("Could not load data from the database, ", error)
    finally:
        if (conn):
            c.close()
            print("The SQLite connection is closed")
            input("Press any key to go back to main menu ")

    return

def Abhishek_CalculateGrossPay():
    try:
        conn = sqlite3.connect('AbhishekDB.db') 
        c = conn.cursor()
        print("Connected to SQLite") 
        c.execute("""SELECT enum,basicPay,ta,hra,comm,overtime from AbhishekTABLE""")# all the records will be stored in c
        
        records = c.fetchall()# to read records from c use fetchall function
 
        print("Total rows are: ", len(records))
        print("Printing each row")

        for col in records:
            print(col[0],col[1],col[2],col[3],col[4],col[5])
            vempno=col[0]
            vBasic= col[1]
            vTA= col[2]
            vHRA=col[3]
            vComm=col[4]
            vOvertime=col[5]
            vGrossPay = vBasic+ vTA + vHRA + vComm + vOvertime
 
            c.execute("UPDATE AbhishekTABLE SET grossPay="+ str(vGrossPay)+" where enum="+str(vempno))
 
            conn.commit()
 
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")
            input("Press any key to go back to main menu ")



def Abhishek_listRecords():
    try:
        conn = sqlite3.connect('AbhishekDB.db') 
        c = conn.cursor()
        print("Connected to SQLite") 

        c.execute("SELECT * from AbhishekTABLE")  # all the records will be stored in c

        records = c.fetchall()  # to read records from c use fetchall function

        print("Total rows are: ", len(records))
        print("Printing each row")

        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("| ENUM | Employee Name | AGE | DEPARTMENT | BASIC PAY | TA | HRA | COMMISION | OT | GROSS PAY | FTAX | PTAX| CPA | NET PAY |")
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------|")

        for col in records:
           print( "| {0:3s} |{1:15s} | {2:3s} | {3:13s}| {4:7s} |{5:5s} |{6:5s}|{7:5s}|{8:7s}|{9:7s}|{10:7s}|{11:7s} |{12:7s} | {13:7s} |".\
                format(str(col[0]),str(col[1]),str(col[2]),str(col[3]),str(col[4]),str(col[5]),str(col[6]),\
                str(col[7]),str(col[8]),str(col[9]),str(col[10]),str(col[11]),str(col[12]),str(col[13])))

        print("-------------------------------------------------------------------------------------------------------------------------------")


    except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
    finally:
            if (conn):
              conn.close()
              print("The SQLite connection is closed")
    input("Press any key to go back to main menu ")


def Abhishek_searcRec():
    try:
        conn = sqlite3.connect('AbhishekDB.db') 
        c = conn.cursor()
        print("Connected to SQLite") 

        no = int(input("Enter the employee number to search"))

        c.execute("SELECT * from AbhishekTABLE where enum=" + str(no))  # all the records will be stored in c

        records = c.fetchall()  # to read records from c use fetchall function

        print("Total rows are: ", len(records))
        print("Printing each row")
        
        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("| ENUM | Employee Name | AGE |  DEPARTMENT  |  BASIC PAY | TA  | HRA | COMMISION | OT | GROSS PAY | FTAX | PTAX| CPA | NET PAY |")
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------|")

        for col in records:
            print( "| {0:3s} |{1:15s} | {2:3s} | {3:13s}| {4:8s} |{5:5s} |{6:5s}|{7:5s}|{8:7s}|{9:7s}|{10:7s}|{11:7s} |{12:7s} | {13:7s} |".\
                format(str(col[0]),str(col[1]),str(col[2]),str(col[3]),str(col[4]),str(col[5]),str(col[6]),\
                str(col[7]),str(col[8]),str(col[9]),str(col[10]),str(col[11]),str(col[12]),str(col[13])))
        
        print("-------------------------------------------------------------------------------------------------------------------------------")

    except sqlite3.Error as err:
        print("Could not load data from database, ", err)

    finally:
        if(conn):
            c.close()
            print("The SQLite connection is closed")
            input("Press any key to go back to main menu ")


def Abhishek_delRec():
    try:
        conn = sqlite3.connect('AbhishekDB.db')
        c = conn.cursor()
        print("Connected to SQLite")

        c.execute("SELECT * from AbhishekTABLE ")

        records = c.fetchall()

        print("Total rows are: ", len(records))

        no = int(input("Enter the employee number to search"))
        c.execute("DELETE FROM AbhishekTABLE WHERE enum=" + str(no)) #the records will be deleted

        # commit
        conn.commit()
    
    except sqlite3.Error as err:
        print("Could not read data form the Database, ", err)
   
    finally:
        if(conn):
            c.close()
            print("The SQLite connection is closed")
            input("Press any key to go back to main menu ")

def Abhishek_CalculateNetPay():
    try:
        conn = sqlite3.connect('AbhishekDB.db') 
        c = conn.cursor()
        print("Connected to SQLite") 
        
        c.execute("SELECT enum,ftax,ptax,cpa,grossPay from AbhishekTABLE")# all the records will be stored in c
        
        records = c.fetchall()# to read records from c use fetchall function
 
        print("Total rows are: ", len(records))
        print("Printing each row")

        for col in records:
            print(col[0],col[1],col[2],col[3],col[4],)
            vempno=col[0]
            vFTax= col[1]
            vPTax= col[2]
            vCPA=col[3]
            vGrossPay=col[4]
            vNetPay = vGrossPay - (vFTax + vPTax + vCPA)

            c.execute("UPDATE AbhishekTABLE SET netPay="+ str(vNetPay)+" where enum="+str(vempno))
 
            conn.commit()

    except sqlite3.Error as err:
        print("Could not load data from database, ", err)

    finally:
        if(conn):
            c.close()
            print("The SQLite connection is closed")
            input("Press any key to go back to main menu ")