import validation
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="hotelmanagement",
    username='root',
    password='',
)

choice = int(input("Want to Signup? Press 1\nFor Login Press 2"))

if choice == 1:
    usr = input("Enter Username :- ")
    psd = input("Enter Password :- ")
    validation.Validation(mydb, usr, psd).new_guest_signup()
else:
    usr = input("Enter Username :- ")
    psd = input("Enter Password :- ")
    validation.Validation(mydb, usr, psd).upval()

