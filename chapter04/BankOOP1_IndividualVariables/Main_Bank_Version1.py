# Test program using accounts
# Version 1, using explicit variables for each Account object

# Bring in all the code from the Account class file
from Account import *

# Create two accounts
oJoesAccount = Account("Joe", 100, "JoesPassword")
print("Created an account for Mary")

oRaphaelsAccount = Account("Raphael", 500, "RaphaelsPassword")
print("Created an account for Raphael")
print()

oJoesAccount.show()
oRaphaelsAccount.show()
print()

# Call some methods on the different accounts
print("Calling methods of the two accounts ...")
oJoesAccount.deposit(50, "JoesPassword")
oRaphaelsAccount.withdraw(345, "RaphaelsPassword")
print()

# Show the accounts
oJoesAccount.show()
oRaphaelsAccount.show()
print()

# Create another account interactively with information from the user
userName = input("What is the nawe for the new user account?")
userBalance = input("What is the starting balance for this acount?")
userBalance = int(userBalance)  # cast to integer
userPassword = input("What is the password you want to use for this account?")
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Let's deposit 100 into the new account
oNewAccount.deposit(100, userPassword)
print()
print("After depositing 100, the user's balance is:", userBalance)

oNewAccount.show()
