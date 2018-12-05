import psycopg2

def logTransaction(amt, typ):
    conn = psycopg2.connect("dbname=postgres user=postgres password=j041050916")
    cur = conn.cursor()
    query = "INSERT INTO tLog (amt, type) VALUES ('%s', %r);" % (amt, typ)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def getTransaction():
    conf = 1

    while conf:
        amt = input ("Transaction amt:  ")
        typ = input("Transaction type dep(1) wit(2):  ")
        conf = confirm(amt, typ)
    logTransaction(amt, typ)

    updateTot(amt, typ)



def confirm(amt, typ):
    transactionType = ""
    if typ == 0:
        transactionType = "deposit"
    else:
        transactionType = "withdrawal"
    

    print ("Confirm: Adding a %s to the log of amount %d") % (transactionType, amt)
    answer = input("Y(1) or N(2):  ")

    if answer == 1:
        return 0
    else:
        return 1

def startBudget():
    print ("log Transaction (1)")
    print ("Generate Report (2)")
    answer = input ("Selection:  ")
    if answer == 1:
        getTransaction()

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






