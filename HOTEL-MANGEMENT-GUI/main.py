import validation
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="hotelmanagement",
    username='root',
    password='',
)

usr = input("Enter Username :- ")
psd = input("Enter Password :- ")

validation.Validation(mydb, usr, psd).upval()

