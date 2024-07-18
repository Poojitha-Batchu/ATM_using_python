from Admin import Admin

class User:

    admin = Admin()

    #existUser method - if the user exists, the following will be displayed
    def userMenu(self):
        acctNo = input("Enter your account number: ")

        if self.checkUser(acctNo):
            while True:
                print("\n---------- USER PORTAL ----------")
                print("1. Check Balance \n2. Deposit money \n3. Withdraw Money \n4. Exit")
                ch = int(input("\nEnter your choice: "))

                if ch == 1: 
                    pin = input("Enter your pin: ")
                    self.printBalance(acctNo, pin)
                elif ch == 2:
                    self.depositMoney(acctNo)
                elif ch == 3:
                    self.withdrawMoney(acctNo)
                elif ch == 4:
                    return
                else:
                    print("Invalid option.. Please try again")                    
                    ch = int(input("Enter your choice: "))
        else:
            print("User not exists.. Please create a account..!!")

    #deposit money method- user enters the deposit money and it adds to its respective avaliable money
    def depositMoney(self, acctNo):
        pin = input("Enter your pin: ")
        valid, balance = self.isValidPin(acctNo, pin)

        if valid:
            depositAmount = int(input("\nEnter the amount to deposit: "))
            if (depositAmount < 0):
                print("Incorrect deposit amount")
            elif (depositAmount == 0):
                print("Deposit amount cannot be zero")
            else:
                twoThousand = int(input("Enter number of 2000 notes: "))
                fiveHundred = int(input("Enter number of 500 notes: "))
                twoHundred = int(input("Enter number of 200 notes: "))
                oneHundred = int(input("Enter number of 100 notes: "))
                notes = [twoThousand, fiveHundred, twoHundred, oneHundred]

                total = (2000 * twoThousand) + (500 * fiveHundred) + (200 * twoHundred) + (100 * oneHundred)
                if total == depositAmount:
                    bal = balance + depositAmount
                    self.updateBalance(acctNo, bal)
                    self.printBalance(acctNo, pin)
                    self.admin.updateNotes("add", notes)
                    self.admin.printNotes()
                else:
                    print("The total amount of notes and the deposited money do not match. Please try again.!!")
        else:
            print("Invalid pin.. Please Enter the valid pin..!!")

    #withdraw money method- 
    def withdrawMoney(self, acctNo):
        pin = input("Enter your pin: ")
        valid , balance = self.isValidPin(acctNo, pin)
        notes = [2000, 500, 200, 100]

        notes_data = self.admin.readNotesFile()
        totalBal = 0

        for n, m in zip(notes_data, notes):
            totalBal += int(n) * m
        
        print("Total amount in ATM: ", totalBal)

        if valid:
            withdrawMoney = int(input("\nEnter withdraw money: "))

            if (withdrawMoney > balance or withdrawMoney <= 0 or withdrawMoney > totalBal):
                print("Incorrect or insufficient funds")
            elif (totalBal == 0):
                print("ATM is empty")
            else:
                update_notes = []

                for note in notes:
                    n = withdrawMoney // note
                    balance -= (n * note)
                    withdrawMoney %= note
                    update_notes.append(n)
                
                self.updateBalance(acctNo, balance)
                print("Withdrawal money as")
                print("2000: %d \n500: %d \n200: %d \n100: %d" %(update_notes[0], update_notes[1], update_notes[2], update_notes[3]))
                self.admin.updateNotes("subtract", update_notes)
                self.admin.printNotes()
                
        else:
            print("Invalid pin.. Please Enter the valid pin..!!")

    #check balance method- printing balance of given account number
    def printBalance(self, acctNo, pin):
        valid , balance = self.isValidPin(acctNo, pin)
        if valid:
            print("\nTotal amount in your account: ", balance)
        else:
            print("Invalid pin.. Please Enter the valid pin..!!")

 #  checkUser method - checks if the user is already exists or not
    def checkUser(self, acctNo):
        exists = False
        
        user_data = self.readUserFile()
        for el in user_data:
            if el[1] == acctNo:
                print("user exists")
                exists = True
                break
        
        return exists
    
    #isValidPin method - checking.. is the pin present in users.txt
    def isValidPin(self, acctNo, pin):
        validPin = False
        bal = 0

        user_data = self.readUserFile()
        for el in user_data:
            if el[2] == pin and el[1] == acctNo:
                print("Pin matched..")
                validPin = True
                bal = el[3]
                break
        
        return validPin, int(bal)
    
    #readFile method- reading users.txt and storing the each line as a list in user_data list
    def readUserFile(self):
        file = open("users.txt", "r")
        user_data = []

        for line in file.readlines():
            user_data.append([elem.strip() for elem in line.split(',')])
        return user_data
        
    #updating balance method- updating amount in respective account
    def updateBalance(self, acctNo, amount):
        user_data = self.readUserFile()

        for el in user_data:
            if acctNo == el[1]:
                el[3] = str(amount)
        
        file = open("users.txt","w")
        for line in user_data:
            s = line[0]+","+line[1]+","+line[2]+","+line[3]+"\n"
            file.write(s)
        print("Balance Updated..!!")
      
        
