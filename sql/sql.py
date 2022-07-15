import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="python",
    username='root',
    password='',
)

choice = int(input("1. Insert\n"
                   "2. Update\n"
                   "3. Delete\n"))

mycursor = mydb.cursor()
if choice == 1:
    st1 = input("Enter student name :- ")
    ot1 = input("Enter other :- ")
    query = "INSERT INTO testing VALUES(%s,%s);"
    mycursor.execute(query,(st1,ot1))
    mydb.commit()
    print(mycursor.rowcount,"raw inserted")
elif choice == 2:
    st1 = input("Enter student name :- ")
    ot1 = input("Enter other :- ")
    query = "UPDATE testing SET oth = %s WHERE name = %s"
    mycursor.execute(query,(st1,ot1))
    mydb.commit()
    print(mycursor.rowcount,"raw updated")
elif choice == 3:
    st1 = input("Enter student name :- ")
    query = "DELETE FROM testing WHERE name = %s"
    mycursor.execute(query,(st1,))
    mydb.commit()
    print(mycursor.rowcount,"raw deleted")
