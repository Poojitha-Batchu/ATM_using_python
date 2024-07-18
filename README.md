# ATM_using_python

This project implements a console-based ATM (Automated Teller Machine) system using Python, leveraging Object-Oriented Programming (OOP) concepts. It allows both users and administrators to perform specific actions related to banking operations and ATM management.

## Features
### User Operations:
1. Withdraw: Allows users to withdraw funds from their account.
2. Deposit: Enables users to deposit funds into their account.
3. Check Balance: Displays the current balance of the user's account.
4. Exit: Allows users to exit the ATM interface.
   
### Admin Operations:
1. Add Money: Allows administrators to add funds to the ATM.
2. Check ATM Balance: Displays the total balance available in the ATM.
3. Check Note Counts: Shows the number of notes available for each denomination (1000, 500, 200, 100).
4. Exit: Allows administrators to exit the admin interface

### Data Storage:
1. User Data: Stored in user.txt file in comma-separated format (username, account number, PIN, balance).
2. ATM Notes: Stored in notes.txt file in comma-separated format (number of 1000, 500, 200, 100 notes).

### Implementation Details:

Classes Used:
1. User: Represents a user with attributes and methods for managing account operations.
2. Admin: Handles administrative tasks such as adding money, checking ATM status, and note counts.
