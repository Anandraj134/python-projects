import room_details


class GuestInformation:
    def __init__(self, mydb, n, a, m, r):
        self.mydb = mydb
        self.n = n
        self.a = a
        self.m = m
        self.r = r

    def guest_info(self):
        mycursor = self.mydb.cursor()
        print("""
    1. Get Guest Information by Mobile Number
    2. Get Guest Information by Room Number
        """)
        choice = int(input("Enter your choice :- "))
        if choice == 1:
            mobno = input("Enter Mobile Number :- ")
            query = "SELECT name, addr, mobile, rno FROM current_guest where mobile = %s"
            mycursor.execute(query, (mobno,))
            result = mycursor.fetchall()
            for i in result:
                name, addr, mobile, rno = i
                print("Name :- {0}\nAddress :- {1}\nMobile Number :- {2}\nRoom Number :- {3}"
                      .format(name, addr, mobile, rno))
        elif choice == 2:
            room = input("Enter Room Number :- ")
            query = "SELECT name, addr, mobile, rno FROM current_guest where rno = %s"
            mycursor.execute(query, (room,))
            result = mycursor.fetchall()
            for i in result:
                name, addr, mobile, rno = i
                print("Name :- {0}\nAddress :- {1}\nMobile Number :- {2}\nRoom Number :- {3}"
                      .format(name, addr, mobile, rno))
        else:
            print("Enter Valid Choice.")

    def add_guest_info(self):
        bill = 0
        mycursor = self.mydb.cursor()
        day = int(input("Enter days you want to stay :- "))
        query = "SELECT price from rooms where rno=%s"
        mycursor.execute(query, (self.r, ))
        price = mycursor.fetchall()
        for i in price:
            temp = str(i)[2:-3]
            bill += (int(temp) * day)

        query = "INSERT INTO current_guest VALUES (%s, %s, %s, %s, %s, %s)"
        print("""
        5 Star Hotel
        Contact No. - 123456789
        Address: Goa
        
        Name :- {0}
        Address :- {1}
        Mobile Number :- {2}
        Price Per Night :- {3}
        Other Charges :- {4}
        Total :- {5}
        """.format(self.n, self.a, self.m, (bill/day), (((bill/day)*18)/100), bill+((bill*18)/100)))
        mycursor.execute(query, (self.n, self.a, self.m, self.r, day, bill))
        self.mydb.commit()
        room_details.room_details(self.mydb, self.r, "").room_allocation()
        print("Guest Information Inserted")

    def remove_guset_info(self):
        mycursor = self.mydb.cursor()
        query = "INSERT INTO old_guest select * from current_guest where rno=%s"
        mycursor.execute(query, (self.r,))
        query = "DELETE FROM current_guest where rno=%s"
        mycursor.execute(query, (self.r,))
        self.mydb.commit()
        room_details.room_details(self.mydb, self.r, "").room_deallocation()
        print("Guest Sucessfully Checked Out.")
