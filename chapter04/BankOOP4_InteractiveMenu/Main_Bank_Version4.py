#!/usr/bin/python3
from Account import *

# print("give me a bottle of rum!")

accountsDict = {}
nextAccountNumber = 0
# --- snip creating accounts, adding them to dictionary ---
oAccount = Account("Joe", 12345, "Joespassword")
joesAccountNumber = nextAccountNumber
# Add account to empty dictionary; With accountnumber as the ID
accountsDict[joesAccountNumber] = oAccount
# Check the account number for the first account
print("Account number for Joe is:", joesAccountNumber)
# Iterate to the next account number to avoid doubles
nextAccountNumber = nextAccountNumber + 1

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("press q to quit")
    print()

    action = input("What do you want to do?")
    action = action.lower()  # grab the first letter
    action = action[0]
    print()
    if action == "b":
        print("*** Get Balance ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print("Your balance is: ", theBalance)

    elif action == "d":
        print("*** Make a new Deposit ***")
        userAccountNumber = input("PLease enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Please enter the password")
        userDepositAmount = input("PLease enter the amount to deposit")
        userDepositAmount = int(userDepositAmount)
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print("Your new balance is: ", theBalance)

    elif action == "o":
        print("*** Open Account ***")
        userName = input("What is the name for the new user account? ")
        userStartingAmount = input("What is the starting balance for this account?")
        userStartingAmount = int(userStartingAmount)
        userPassword = input("What is the desired password for this account?")
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif action == "s":
        print("Show:")
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print("     Account number: ", userAccountNumber)
            oAccount.show()

    elif action == "q":
        break

    elif action == "w":
        print("*** Witdhraw ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input("Please enter the amount you wish to withdraw: ")
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input(
            f"Please enter the password for account number, {userAccountNumber}: "
        )
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.userWithdrawalAmount(userWithdrawalAmount, userPassword)

        if theBalance is not None:
            print("Withdrew:", userWithdrawalAmount)
            print("Your new balance is:", theBalance)
        else:
            print("Insufficient funds.")

print("Done")
