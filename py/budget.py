import psycopg2
import datetime


#Upon recieving a new transaction, this function will insert the record into the database
def logTransaction(amt, typ, day, month, year):
    conn = psycopg2.connect("dbname=postgres user=postgres password=j041050916")
    cur = conn.cursor()
    print(month,day,year)
    query = "INSERT INTO tLog (amt, type, dt) VALUES (%s, %s, '%s');" % (amt, typ, datetime.date(year,month,day))
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

#Recieves user input for transaction information (ie. Deposit/Withdrawal, Amt, and Date)
#TODO 
#Add date parameter to both py and DB table
def getTransaction():
    conf = 1

    while conf:
        amt = (input ("Transaction amt:  "))
        typ = (input("Transaction type dep(1) wit(2):  "))
        dt = input("Was this transaction completed today? (y) (n): ")

        if dt == "y":
            x = datetime.datetime.now()
            month = int(x.strftime("%m")) 
            day = int(x.strftime("%d"))
            year =  int(x.strftime("%Y"))
        else:
            day = int(input ("Day: "))
            month = int(input ("Month: "))
            year = int(input ("Year: "))
        conf = confirm(amt, typ, day, month, year)
    logTransaction(amt, typ, day, month, year)

    updateTot(amt, typ)


#Confirmation of transaction before being commited
def confirm(amt, typ, day, month, year):
    transactionType = ""
    if typ == "0":
        transactionType = "deposit"
    else:
        transactionType = "withdrawal"

    print ("Confirm: Adding a %s to the log of amount %s for date %s/%s/%s" % (transactionType, amt, month, day, year))
    answer = input("Y(1) or N(2):  ")

    if answer == "1":
        return 0
    else:
        return 1


#Kicks off the Budget Module, Controls flow between different aspects of the module
def startBudget():
    print ("log Transaction (1)")
    print ("View Reports (2)")
    answer = input ("Selection:  ")
    if answer == "1":
        getTransaction()
    if answer == "2":
        reports()


#Updates the total funds amt in a csv file
#TODO: Add table to DB to store this value (Daily Totals?)
def updateTot(amt, typ):
    f = open("tot.csv", "r+")
    a = float(f.readline())
    
    if type == 1:
        temp = a + amt
    else:
        temp = a - amt
    
    f.seek(0,0)
    f.write(str(temp))
    f.close()

#Selection module for different report types for the budget
def reports():
    print("Select Report Type: ")
    print("Transaction Log (1) ")
    answer = input ("Selection: ")

    if answer == 1:
        transLog()


def queryLog(length):
    conn = psycopg2.connect("dbname=postgres user=postgres password=j041050916")
    cur = conn.cursor()
    query = "SELECT * FROM tlog;"
    cur.execute(query)
    for record in cur:
        print (record)
    conn.commit()
    cur.close()
    conn.close()

def transLog():
    print("Select Length of Report: ")
    print("Day   (1)")
    print("Month (2)")
    print("All   (3)")
    length = input ("Selection: ")

    print("Generating Report...")

    #response = queryLog(1)




    





