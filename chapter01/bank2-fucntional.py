# Non-OOP
# Bank 2
# Single account

accountName = ''
accountBalance = 0
accountPassword = ''

# Functions for each of the operations that we identified for a bank account.
# Create, Check balance, Deposit and Withdraw

def newAccount(name, balance, password):
	global accountName, accountBalance, accountPassword
	accountName = name
	accountBalance = balance
	accountPassword = password

def show():
	global accountName, accountBalance, accountPassword
	print('		Name', accountName)
	print('		Balance:', accountBalance)
	print('		Password:', accountPassword)
	print()

def getBalance(password):
	global accountName, accountBalance, accountPassword
	if password != accountPassword:
		print('Incorrect password')
		return None
	return accountBalance

def deposit(amountToDeposit, password):
	global accountName, accountBalance, accountPassword
	if amountToDeposit < 0:
		print('You cannot deposit a negative amount!')
		return None

	if password != accountPassword:
		print('Incorrect password')
		return None

	accountBalance = accountBalance + amountToDeposit
	return accountBalance

def withdraw(amountToWithdraw, password):
	global accountName, accountBalance, accountPassword
	if amountToWithdraw < 0:
		print('You cannot withdraw a negative amount')
		return None

	if password != accountPassword:
		print('Incorrect password for this account')
		return None

	accountBalance = accountBalance - amountToWithdraw
	return accountBalance


newAccount("Joe", 100, 'soup')

# Main code

while True:
	print()
	print('Press b to get the balance')
	print('Press d to make a deposit')
	print('Press w to make a withdrawal')
	print('Press s to show the account')
	print('Press q to quit')
	print()

	action = input('What do you want to do? ')
	action = action.lower()
	action = action[0]
	print()

	if action == 'b':
		print('Get Balance:')
		userPassword = input('Please enter the password: ')
		theBalance = getBalance(userPassword)
		if theBalance is not None:
			print('Your balance is', theBalance)

	elif action == 'd':
		print('Deposit:')
		userDepositAmount = input('Please enter amount to deposit: ')
		userDepositAmount =  int(userDepositAmount)
		userPassword = input('please enter the password: ')

		newBalance = deposit(userDepositAmount, userPassword)
		if newBalance is not None:
			print('Your new balance is:', newBalance)

	elif action == 'w':
		print('Withdraw:')
		userPassword = input('Please enter the password: ')
		userWithdrawAmount = input('Please enter amount to withdraw')
		userWithdrawAmount = int(userWithdrawAmount)
		
		newBalance = withdraw(userWithdrawAmount, userPassword)
		if newBalance is not None:
			print('Your new balance is:', newBalance)

	elif action == 's':
		print('Show:')
		show()

	elif action == 'q':
		break




print('Done')