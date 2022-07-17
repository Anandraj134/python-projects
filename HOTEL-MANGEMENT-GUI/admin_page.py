import room_details
import guest
import validation

def admin(mydb):
    print("""
    1. Room Detail
    2. Check in
    3. Check out
    4. Guest Information
    5. Get Allocated Room list
    6. Get Unallocated Room List
    7. Update Room Number
    8. Update Password
    9. Add New Employee
    10. Add New Admin    
    """)

    choice = int(input("Enter Your Choice :- "))

    if choice == 1:
        room = int(input("Enter Room Number :- "))
        room_details.room_details(mydb, room, "").room()
    elif choice == 2:
        name = input("Enter Guest Name :- ")
        addr = input("Enter Address :- ")
        mobile = input("Enter mobile Number :- ")
        guest.GuestInformation(mydb, name, "", mobile, "").guest_visit_count()
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
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    else:
        print("Enter Valid Choice")