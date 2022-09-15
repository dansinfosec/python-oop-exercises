from Account import *

# Dict		> Key (ID)			: > Value (Object)
# Dict		> Key (ID)			: > Value (Object)


accountsDict = {}  # Empty dictionary
nextAccountNumber = 0  # Instantiate count from 0

# Create first account
oAccount = Account("Joe", 12345, "Joespassword")
joesAccountNumber = nextAccountNumber
# Add account to empty dictionary; With accountnumber as the ID
accountsDict[joesAccountNumber] = oAccount
# Check the account number for the first account
print("Account number for Joe is:", joesAccountNumber)
# Iterate to the next account number to avoid doubles
nextAccountNumber = nextAccountNumber + 1

# Create the second account
oAccount = Account("Mary", 100, "Maryspassword")
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print("Account number for Mary is:", marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1


# Show the newly created accounts
accountsDict[joesAccountNumber].show()
print()
accountsDict[marysAccountNumber].show()
print()

# Create another account with information from the user
print()
# Ask input and store in variales userName, userBalance and userPassword
userName = input("What is the name for the new user account? ")
userBalance = input("What is the starting balance for this account? ")
userBalance = int(userBalance)  # Cast to Integer
userPassword = input("What is the password you want to use for this account? ")

# Actually fill in the arguments from the Account class and store in a new object
oAccount = Account(userName, userBalance, userPassword)

# Dont forget the ID so you dont get into trouble with your Dataset
# You already iterated after you have created the previous account
newAccountNumber = nextAccountNumber

# Store the object with the ID as a key value pair in a dictionary
# Dict		> Key (ID)			: > Value (Object)
accountsDict[newAccountNumber] = oAccount

# Debug test the account number correct ID
print("Account number for new account is: ", newAccountNumber)

# Iterate account number for next account
nextAccountNumber = nextAccountNumber + 1

# Show the newly created user account (Calling some methods)
accountsDict[newAccountNumber].show()
accountsDict[newAccountNumber].deposit(100, userPassword)

# Get the balance and save it in variable usersBalance
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is: ", usersBalance)
accountsDict[newAccountNumber].show()
