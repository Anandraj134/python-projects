import admin_page
import emp_page
import guest_page
import psdval


class Validation:

    def __init__(self,mydb, username, pswd):
       self.mydb = mydb
       self.username = username
       self.pswd = pswd

    def upval(self):
        mycursor = self.mydb.cursor()
        query = "SELECT password, type FROM validation where username=%s"
        mycursor.execute(query, (self.username, ))
        result = mycursor.fetchall()
        psd, type = result[0]
        if self.pswd == psd:
            print("""
Hello {0},
You Successfully logged in
                            """.format(self.username))
            if type == "admin":
                admin_page.admin(self.mydb)
            elif type == "emp":
                emp_page.employee(self.mydb)
            else:
                guest_page.guestPage(self.mydb)

    def new_guest_signup(self):
        mycursor = self.mydb.cursor()
        validpsd = psdval.password_check(self.pswd)
        if validpsd:
            query = "INSERT INTO validation VALUES (%s, %s, 'guest')"
            mycursor.execute(query, (self.username, self.pswd))
            self.mydb.commit()
            guest_page.guestPage(self.mydb)
        else:
            while True:
                pswd = input("Enter Password Again :- ")
                validpsd = psdval.password_check(pswd)
                if validpsd:
                    query = "INSERT INTO validation VALUES (%s, %s, 'guest')"
                    mycursor.execute(query, (self.username, self.pswd))
                    self.mydb.commit()
                    guest_page.guestPage(self.mydb)

    def new_admin_signup(self):
        mycursor = self.mydb.cursor()
        validpsd = psdval.password_check(self.pswd)
        if validpsd:
            query = "INSERT INTO validation VALUES (%s, %s, 'admin')"
            mycursor.execute(query, (self.username, self.pswd))
            self.mydb.commit()
            print("Admin Added Successfully")
        else:
            while True:
                pswd = input("Enter Password Again :- ")
                validpsd = psdval.password_check(pswd)
                if validpsd:
                    query = "INSERT INTO validation VALUES (%s, %s, 'admin')"
                    mycursor.execute(query, (self.username, self.pswd))
                    self.mydb.commit()
                    print("Admin Added Successfully")

    def new_emp_signup(self):
        mycursor = self.mydb.cursor()
        validpsd = psdval.password_check(self.pswd)
        if validpsd:
            query = "INSERT INTO validation VALUES (%s, %s, 'emp')"
            mycursor.execute(query, (self.username, self.pswd))
            self.mydb.commit()
            print("Employee Added Successfully")
        else:
            while True:
                pswd = input("Enter Password Again :- ")
                validpsd = psdval.password_check(pswd)
                if validpsd:
                    query = "INSERT INTO validation VALUES (%s, %s, 'emp')"
                    mycursor.execute(query, (self.username, self.pswd))
                    self.mydb.commit()
                    print("Employee Added Successfully")

    def pass_change(self):
        mycursor = self.mydb.cursor()
        query = "UPDATE validation SET password = %s WHERE username = %s"
        mycursor.execute(query, (self.pswd, self.username))
        self.mydb.commit()
        print("Password Changed Successfully.")
