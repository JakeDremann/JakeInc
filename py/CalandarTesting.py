from task import item
import psycopg2

def newTask(title = "", priority = None ):
    if (title == ""):
        title = input("Title: ")
    if (priority == None):
        priority = input("Priority: ")

    newTask = item()
    newTask.setTitle(title)
    newTask.setPriority(priority)

    saveTask(newTask)

def saveTask(newTask):
    conn = psycopg2.connect("dbname=postgres user=postgres password=j041050916")
    cur = conn.cursor()
    query = "INSERT INTO tasks (title, priority) VALUES ('%s', %d);" % (newTask.title, newTask.priority)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

#Takes the title of a task and deletes if from the table
def deleteTask(TTD):
    if TTD == "":
        TTD = input("Task to Delete: ")
    conn = psycopg2.connect("dbname=postgres user=postgres password=j041050916")
    cur = conn.cursor()
    query = "DELETE FROM tasks WHERE TITLE = '%s'" % (TTD)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def getTasks():
    return 0 

deleteTask("Test")
        
        

    





