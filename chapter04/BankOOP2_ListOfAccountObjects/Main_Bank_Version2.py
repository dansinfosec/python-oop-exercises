# Test program using accounts
# Version 2, using a list of acounts

# Bring in all the code from the Account class file
from Account import *

# Start off with an empty list of accounts
accountsList = []

# Create two accounts
oAccount = Account("Joe", 100, "JoesPassword")
accountsList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account("Mary", 12345, "Maryspassword")
accountsList.append(oAccount)
print("Mary's account number is 1")

accountsList[0].show()
accountsList[1].show()
print()

# Call some methods on different accounts
print("Calling methods of the two accounts..")
accountsList[0].deposit(50, "JoesPassword")
accountsList[1].deposit(345, "Maryspassword")
accountsList[1].deposit(100, "Maryspassword")

# Show the accounts
accountsList[0].show()
accountsList[1].show()


# Create another account with the information is the user


userName = input("What is the nawe for the new user account?")
userBalance = input("What is the starting balance for this acount?")
userBalance = int(userBalance)  # cast to integer
userPassword = input("What is the password you want to use for this account?")
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

accountNumber = int(len(accountsList)) - 1

print("Created new account, account number is:", accountNumber)

# Show the new account
accountsList[accountNumber].show()


# This approach has some serious flaws; Let's say we .pop() or delete().
# The indexes will be seriously fucked
# To handle a large numbers of objects we generally use a dictionary

# {0 : <object for account 0>, 1 : <object for account 1>, ... }

# Primary Key; Identifier... Lots of similarities with ORM
