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
        print("Guest Successfully Checked Out.")

    def guest_visit_count(self):
        count = 0
        mycursor = self.mydb.cursor()
        query = "SELECT COUNT(mobile) FROM old_guest WHERE mobile=%s"
        mycursor.execute(query, (self.m, ))
        temp = mycursor.fetchall()
        for i in temp:
            cnt = str(i)[1:-2]
            count += int(cnt)
        if count > 0:
            print("{0} Visits {1} times".format(self.n, count))
        else:
            print("{0} is Visit for the First Time".format(self.n))

    def guest_advance_booking(self, date, day):
        mycursor = self.mydb.cursor()
        query = "INSERT INTO advance_booking VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(query, (self.n, self.a, self.m, day, date, self.r))
        self.mydb.commit()
        print("{0}, Your Room is successfully booked for {1}".format(self.n, date))

    def cancle_advance_booking(self, date):
        mycursor = self.mydb.cursor()
        query = "INSERT INTO cancle_advance_booking select * from advance_booking where mobile=%s and date=%s"
        mycursor.execute(query, (self.m, date))
        query = "DELETE FROM advance_booking where mobile=%s and date=%s"
        mycursor.execute(query, (self.m, date))
        self.mydb.commit()
        print("Your Room is successfully cancelled for {0}".format(date))

    def change_room(self):
        room = input("Enter New Room Number :- ")
        mycursor = self.mydb.cursor()
        query = "UPDATE rooms SET allocated = 'No' where rno=%s"
        mycursor.execute(query, (self.r, ))
        query = "UPDATE rooms SET allocated = 'Yes' where rno=%s"
        mycursor.execute(query, (room, ))
        query = "UPDATE current_guest SET rno = %s WHERE rno = %s"
        mycursor.execute(query, (room, self.r))
        self.mydb.commit()
        print("Room Numer changed successfully.")

