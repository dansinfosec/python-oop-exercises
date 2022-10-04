#!/usr/bin/python3

# print("give me a bottle of rum!")

from Account import *


class Bank:
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input("What is your account number")
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction("The account must be an integer")
        if accountNumber not in self.accountsDict:
            raise AbortTransaction(
                "The account" + str(accountNumber) + "does not exist"
            )
        return accountNumber

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidAccountNumber(oAccount)
        return oAccount

    # def createAccount(self, theName, theStartingAmount, thePassword):
    #     oAccount = Account(theName, theStartingAmount, thePassword)
    #     newAccountNumber = self.nextAccountNumber
    #     self.nextAccountNumbher = 0

    def askForValidPassword(self, oAccount):
        password = input("Please enter your password: ")
        oAccount.checkPasswordMatch(password)

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount

        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print("*** Open Account ***")
        userName = input("What is the name for the new user account? ")
        userStartingAmount = input("How much money do to start your acount? ")
        userPassword = input("What password would you like to use for this account? ")
        userAccountNumber = self.createAccount(
            userName, userStartingAmount, userPassword
        )
        print("Your new account number is:", userAccountNumber)

    def closeAccount(self):
        print("*** Close Account ***")
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        theBalance = oAccount.getBalance()
        print("You had", theBalance, "in your account which is being returned to you.")
        del self.accountsDict[userAccountNumber]
        print("Your account is now closed.")

    def balance(self):
        print("*** Get Balance ***")
        oAccount = self.getUsersAccount()
        theBalance = oAccount.getBalance()
        print("Your balance is:", theBalance)

        # userAccountNumber = input("Please enter your account number: ")
        # userAccountNumber = int(userAccountNumber)
        # userAccountPassword = input("Please enter the password: ")
        # oAccount = self.accountsDict[userAccountNumber]
        # theBalance = oAccount.getBalance(userAccountPassword)
        # if theBalance is not None:
        #     print("Your balance is", theBalance)

    def deposit(self):
        print("*** Deposit ***")
        oAccount = self.getUsersAccount()
        depositAmount = input("Please enter the amount to deposit: ")
        theBalance = oAccount.deposit(depositAmount)
        print("Deposited", depositAmount)
        print("Your new balance is:", theBalance)

    def getInfo(self):
        print("Hours", self.hours)
        print("Address", self.address)
        print("Phone", self.phone)
        print("We currently have", len(self.accountsDict), "account(s) open.")

        # accountNum = input("Please enter the account number: ")
        # accountNum = int(accountNum)
        # depositAmount = input("Please enter the amount to deposit: ")
        # depositAmount = int(depositAmount)
        # userAccountPassword = input("{Please enter the password: ")
        # oAccount = self.accountsDict[accountNum]
        # theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        # if theBalance is not None:
        #     print("Your new balance is:", theBalance)

    # Special method for Bank administrator only
    def show(self):
        print("*** Show ***")
        print("(This would typically require an admin password)")
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print("     Account:", userAccountNumber)
            oAccount.show()
            print()

    def withdraw(self):
        print("*** Withdraw ***")
        oAccount = self.getUsersAccount()
        witdhrawAmount = input("Please enter the amount to withdraw")
        theBalance = oAccount.withdraw(witdhrawAmount)
        print("Witdhrew:", witdhrawAmount)
        print("Your new balance is:", theBalance)
