
class Admin:

    #admin menu method -  admin options
    def adminMenu(self):
        adminId = "admin@123"
        adminPassword = "admin@123"

        # while True:
        Id = input("\nEnter Admin ID: ")

        if (adminId == Id):
            password = input("Enter admin password: ")

            while(adminPassword == password):
                    print("\n---------- ADMIN PORTAL ----------")
                    print("1. Add notes \n2. Print Notes \n3. Exit")
                    ch = int(input("\nEnter your option: "))

                    if(ch == 1):
                        twoThousand = int(input("Enter number of 2000 notes: "))
                        fiveHundred = int(input("Enter number of 500 notes: "))
                        twoHundred = int(input("Enter number of 200 notes: "))
                        oneHundred = int(input("Enter number of 100 notes: "))
                        notes = [twoThousand, fiveHundred, twoHundred, oneHundred]

                        self.updateNotes("add", notes)
                        self.printNotes()
                        
                    elif (ch == 2):
                        self.printNotes()
                    elif (ch == 3):
                        print("Existing...")
                        return
                    else:
                        print("Invalid option.. Please try again")
            else:
                print("Invalid Admin password.. Please try again")
        else:
            print("Invalid Admin ID.. Please try again")
    

    # read note file method- reads the number of each note present in notes.txt
    def readNotesFile(self):
        file = open("notes.txt", "r")
        s = file.readline()

        note_data = [int(ele.strip()) for ele in s.split(",")]
        return note_data


    #update note method- updating each note in notes.txt
    def updateNotes(self, operation, notes):
        note_data = self.readNotesFile()

        if(operation == "add"): 
            note_data[0] += notes[0]
            note_data[1] += notes[1]
            note_data[2] += notes[2]
            note_data[3] += notes[3]
        elif(operation == "subtract"):
            note_data[0] -= notes[0]
            note_data[1] -= notes[1]
            note_data[2] -= notes[2]
            note_data[3] -= notes[3]

        self.writeNotesFile(note_data)
        print("\nNotes are updated in ATM..!!")


    #write notes file - writing the note value in notes.txt
    def writeNotesFile(self, note_data):
        file = open("notes.txt", "w")
        note = str(note_data[0])+","+str(note_data[1])+","+str(note_data[2])+","+str(note_data[3])
        file.writelines(note)


    #print note method- printing number of notes
    def printNotes(self):
        note_data = self.readNotesFile()
        print("Available notes in ATM are: ")
        print("2000: %d, 500: %d, 200: %d, 100: %d" % (note_data[0], note_data[1], note_data[2], note_data[3]))
