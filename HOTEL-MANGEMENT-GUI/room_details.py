class room_details:

    def __init__(self, mydb, rno, types):
        self.mydb = mydb
        self.rno = rno
        self.types = types

    def roomfinder(self):
        mycursor = self.mydb.cursor()
        query = "SELECT rno from rooms where allocated='No' and type=%s"
        mycursor.execute(query, (self.types,))
        result = mycursor.fetchall()
        for i in result:
            print(str(i)[2:-3])

    def room(self):
        mycursor = self.mydb.cursor()
        query = "SELECT rno, type, price, allocated from rooms where rno=%s"
        mycursor.execute(query, (self.rno,))
        result = mycursor.fetchall()
        for i in result:
            rno, rtype, price, allocated = i
            print("Room Number :- {0}\nRoom Type :- {1}\nRoom Price :- {2}\nAllocated :- {3}"
                  .format(rno, rtype, price, allocated))

    def room_allocation(self):
        mycursor = self.mydb.cursor()
        query = "UPDATE rooms SET allocated = 'Yes' where rno=%s"
        mycursor.execute(query, (self.rno, ))
        self.mydb.commit()

    def room_deallocation(self):
        mycursor = self.mydb.cursor()
        query = "UPDATE rooms SET allocated = 'No' where rno=%s"
        mycursor.execute(query, (self.rno, ))
        self.mydb.commit()

    def allocated_room(self):
        mycursor = self.mydb.cursor()
        query = "SELECT rno from rooms where allocated='Yes'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print(str(i)[2:-3])

    def deallocated_room(self):
        mycursor = self.mydb.cursor()
        query = "SELECT rno from rooms where allocated='No'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print(str(i)[2:-3])