import admin_page
import emp_page
import guest_page


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


