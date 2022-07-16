import room_details
import guest
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="hotelmanagement",
    username='root',
    password='',
)

print("""
Welcome to Hotel

1. Room Detail
2. Check in
3. Check out
4. Guest Information
5. Get Allocated Room list
6. Get Unallocated Room List

""")

choice = int(input("Enter Your Choice :- "))

if choice == 1:
    room = int(input("Enter Room Number :- "))
    roomDetails = room_details.room_details(mydb, room, "").room()
elif choice == 2:
    name = input("Enter Guest Name :- ")
    addr = input("Enter Address :- ")
    mobile = input("Enter mobile Number :- ")
    types = input("Super_Delux\nDelux\nGeneral\n")
    room_details.room_details(mydb, "", types.lower()).roomfinder()
    room = input("Enter Room Number :- ")
    guest.GuestInformation(mydb, name, addr, mobile, room).add_guest_info()
elif choice == 3:
    room = input("Enter Room Number :- ")
    guest.GuestInformation(mydb, "", "", "", room).remove_guset_info()
elif choice == 4:
    guest.GuestInformation.guest_info(mydb)
elif choice == 5:
    room_details.room_details(mydb, "", "").allocated_room()
elif choice == 6:
    room_details.room_details(mydb, "", "").deallocated_room()
else:
    print("Enter Valid Choice")
