# Define a custom exception
class AbortTransaction(Exception):
    """raise this exception to abort a blank transaction"""

    pass


class Account:
    """An OOP Aproach to chapter 1's bank-account"""

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction("Amount must be an integer")
        if amount <= 0:
            raise AbortTransaction("Amount must be positive")
        return amount

    def checkPasswordMatch(self, password):
        if password != password:
            raise AbortTransaction("Incorrect Password for this account")

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction(
                "You cannot withdraw more than you have in your account"
            )
        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self):
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
