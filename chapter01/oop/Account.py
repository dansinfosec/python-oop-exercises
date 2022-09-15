# Account class


class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None

        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithDraw, password):
        if password != self.password:
            print("Incorrect password for this account")
            return None

        if amountToWithDraw < 0:
            print("You cannot withdraw a negative amount")
            return None

        if amountToWithDraw > self.balance:
            print("You cannot withdraw more than you have in your account")
            return None

        self.balance = self.balance - amountToWithDraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        return self.balance

    # Added for debugging
    def show(self):
        print("		Name:", self.name)
        print("		Balance:", self.balance)
        print("		Password:", self.password)
        print("")
