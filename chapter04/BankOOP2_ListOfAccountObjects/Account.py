class Account:
    """An OOP Aproach to chapter 1's bank-account"""

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry incorrect password")
            return None

        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Sorry incorrect password")
            return None

        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Sorry incorrect password")
            return None

        return self.balance

    # Added for debugging
    def show(self):
        print("     Name:", self.name)
        print("     Balance:", self.balance)
        print("     Password", self.password)


# # Main code
# oAccount = Account('Joe Schmoe', 1000, 'magic')
# newBalance = oAccount.deposit(500, 'magic')
# oAccount.withdraw(250, 'magic')
# currentBalance = oAccount.getBalance('magic')
# print('Your balance is:', currentBalance)
