import sys
from User import User
from Admin import Admin

def showMenu():

    admin = Admin()
    user = User()

    while True:

        print("\n----- Welcome to ATM (Automated Teller Machine) -----")
        print("1. Admin \n2. User \n3. Exit")
        ch = int(input("\nEnter your option: "))

        if ch == 1:
            admin.adminMenu()
        elif ch == 2:
            user.userMenu()
        elif ch == 3:
            sys.exit(0)
        else:
            print("Invalid option.. Please try again..")
            ch = int(input("Enter your option: "))

if __name__ == "__main__":
    showMenu()
