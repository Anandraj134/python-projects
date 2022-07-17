import room_details
import guest

def guestPage(mydb):
    print("""
        1. Advance Booking
        2. Cancel Advance Booking
        """)

    choice = int(input("Enter Your Choice :- "))

    if choice == 1:
        name = input("Enter Name :- ")
        addr = input("Enter Address :- ")
        mobile = input("Enter mobile Number :- ")
        date = input("Enter Date in DD/MM/YYYY Format :- ")
        day = int(input("Enter days you want to stay :- "))
        print("""
                    Sr.  Room Type       Price Per Night
                     1.  Super Delux        5000
                     2.  Delux              3000
                     3.  General            1000
                    """)
        types = int(input("Enter Your Choice :- "))
        if types == 1:
            room_details.room_details(mydb, "", "super-delux").roomfinder()
        elif types == 2:
            room_details.room_details(mydb, "", "delux").roomfinder()
        elif types == 3:
            room_details.room_details(mydb, "", "general").roomfinder()
        room = input("Enter Room Number :- ")
        guest.GuestInformation(mydb, name, addr, mobile, room).guest_advance_booking(date, day)
    elif choice == 2:
        mobile = input("Enter mobile Number :- ")
        date = input("Enter Date in DD/MM/YYYY Format :- ")
        guest.GuestInformation(mydb, "", "", mobile, "").cancle_advance_booking(date)
        pass
    else:
        print("Enter Valid Choice")