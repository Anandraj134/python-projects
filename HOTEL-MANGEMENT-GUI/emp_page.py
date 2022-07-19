import room_details
import guest
import validation


def employee(mydb):
    print("\n"
          "        1. Room Detail\n"
          "        2. Check in\n"
          "        3. Check out\n"
          "        4. Get Allocated Room list\n"
          "        5. Get Unallocated Room List\n"
          "        6. Change Password\n"
          "        ")

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
        room_details.room_details(mydb, "", "").allocated_room()

    elif choice == 5:
        room_details.room_details(mydb, "", "").deallocated_room()

    elif choice == 6:
        user = input("Enter Username :- ")
        new_pass = input("Enter New Password :- ")
        validation.Validation(mydb, user, new_pass).pass_change()

    else:
        print("Enter Valid Choice")
