#!/usr/bin/python3

# print("give me a bottle of rum!")

from Account import *


class Bank:
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumbher = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumbher
        self.accountsDict[newAccountNumber] = oAccount

        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print("*** Open Account ***")
        userName = input("What is the name for the new user account? ")
        userStartingAmount = input(
            "What is the starting balance for the new user account? "
        )
        userStartingAmount = int(userStartingAmount)
        userPassword = input("What is the password you want to use for this account? ")

        userAccountNumber = self.createAccount(
            userName, userStartingAmount, userPassword
        )
        print("Your new account number is", userAccountNumber)
        print()
