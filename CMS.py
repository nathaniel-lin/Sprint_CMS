"""
CRUD for CMS:

The primary goal of the Courier Service is to:
1. Collect Parcel
2. Keep the record of sender and recipient
3. Tracking of the Parcel

"""

import sqlite3
import sys

#For connecting the database
try:
    cms=sqlite3.connect('CNSS.db')

except sqlite3.OperationalError as e:
    print("Operational Error has occoured while connecting! with a message:")
    print(e)
    sys.exit()

#Returns a Cursor object which uses this Connection
cur=cms.cursor()

# Enable Foreign Key Constraints
cur.execute("PRAGMA foreign_keys = ON")

while True:
    #Menu
    print("-------------------------")
    print("Welcome to Courier Management System ~ Please Select Your Option:")
    print("1.Sender Info")
    print("2.Recipient Info")
    print("3.Parcel")
    print("4.Logout")
    print("-------------------------")
    n=int(input("Enter your choice: "))
    print("-------------------------")

    #Sender
    if n==1:
        print("1.Insert the sender details")
        print("2.Retrieve sender details")
        print("3.Retrieve details of all the senders")
        print("4.Delete the details of a particular sender")
        y=int(input("Enter your choice:"))

        # Used for deleting a record of particular user
        if y==4:
            u=int(input("Enter the sid of the sender"))
            sql10 = "DELETE from sender WHERE sid="+str(u)+";"
            cur.execute(sql10)
            cms.commit()
            print("Deleted the records of sid="+str(u))
        #Retrieve All
        if y==3:
            print("[Sender ID, Sender Name, Sender Address]")
            sql7 = "SELECT * FROM sender;"
            # Execute fun used to run the sql command internally
            cur.execute(sql7)
            while True:
                #Retrieves one result row for the query that was executed on that cursor
                se = cur.fetchone()
                if se == None:
                    break
                print(se)
        #Retrieve particular data
        if y==2:
            z = int(input("Enter the sender id :"))
            print("[Sender ID, Sender Name, Sender Address]")
            sql8 = "SELECT * FROM sender WHERE sid=" + str(z)
            cur.execute(sql8)
            while True:
                send = cur.fetchone()
                if send == None:
                    break
                print(send)
        #Insert the data
        if y==1:
            cur.execute('''CREATE TABLE IF NOT EXISTS sender
                        (sid INTEGER PRIMARY KEY, sname VARCHAR(60), sadd VARCHAR(100))''')
            sid = int(input("Give an id: "))
            nam = input("Enter the name of sender: ")
            sadd = input("Enter the address of sender: ")
            cur.execute("INSERT INTO sender (sid, sname, sadd) VALUES (?,?,?);",
                        (sid, nam, sadd))
            #Used for modifying the data
            cms.commit()
            print("All the sender details were successfully inserted into the database")

    #Recipient
    if n==2:
        print("1.Add an recipient")
        print("2.Retrieve recipient details")
        print("3.Retrieve details of all the recipients")
        k=int(input("Enter your choice: "))

        if k==3:
            print("[Courier Office ID, Recipient Name, Recipient ID]")
            sql4 = "SELECT * FROM emp;"
            cur.execute(sql4)
            while True:
                #retrieves one result row for the query that was executed on that cursor
                empl = cur.fetchone()
                if empl == None:
                    break
                print(empl)

        if k==2:
            i = int(input("Enter the recipient id: "))
            print("[Courier Office ID, Recipient Name, Recipient ID]")
            sql5 = "SELECT * FROM emp WHERE eid=" + str(i)
            cur.execute(sql5)
            while True:
                em = cur.fetchone()
                if em == None:
                    break
                print(em)

        if k==1:
            cur.execute("CREATE TABLE IF NOT EXISTS emp(cid INTEGER PRIMARY KEY, ename VARCHAR(100), eid INT)")
            cid = int(input("Enter the id of courier office: "))
            name = input("Enter the name of recipient: ")
            eid = int(input("Give an ID : "))
            cur.execute("INSERT INTO emp (cid, ename, eid) VALUES (?,?,?);",
                        (cid, name, eid))
            cms.commit()
            print("All the recipient details were successfully inserted into the database")

    #Parcel
    if n==3:
        print("1.Insert")
        print("2.Collect parcel details")
        print("3.Retrieve details of all the parcels")
        print("4.Delete the details of a particular parcel")
        j=int(input("Enter your choice: "))

        if j==4:
            h=int(input("Enter the parcel id(pid)"))
            sql11 = "DELETE FROM parcel WHERE pid="+str(h)
            cur.execute(sql11)
            cms.commit()

        if j==1:
            cur.execute('''CREATE TABLE IF NOT EXISTS parcel 
                        (pid INTEGER PRIMARY KEY, sid INT, cid INT, radd VARCHAR(100) , bill_amt INT)''')
            pid=int(input("Enter the parcel id :"))
            sid=int(input("Enter the sender id :"))
            cid=int(input("Enter the courier office id :"))
            add=input("Enter receiver's address : ")
            amt=int(input("Billing amount :"))
            cur.execute("INSERT INTO parcel (pid,sid,cid,radd,bill_amt) VALUES (?,?,?,?,?);",(pid,sid,cid,add,amt))
            cms.commit()
            print("All the parcel details were successfully inserted into the database")

        if j==2:
            x=int(input("Please enter the sender ID:"))
            print("[Parcel ID, Sender ID, Courier Office ID, Receiver's Address, Billing Amt]")
            sql3 = "SELECT * FROM parcel WHERE sid="+str(x)
            cur.execute(sql3)
            while True:
                parcel = cur.fetchone()
                if parcel == None:
                    break
                print(parcel)

        if j==3:
            print("[Parcel ID, Sender ID, Courier Office ID, Receiver's Address, Billing Amt]")
            sql6 = "SELECT * FROM parcel;"
            cur.execute(sql6)
            while True:
                pk = cur.fetchone()
                if pk == None:
                    break
                print(pk)

    #Logout
    if n==4:
        print("Hand it to us, we're good  :)")
        cms.close()
        break

#End
