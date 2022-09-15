# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

accountNamesList= []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
	global accountNamesList, accountBalancesList, accountPasswordsList
	accountNamesList.append(name)
	accountBalancesList.append(balance)
	accountPasswordsList.append(password)

def show(accountNumber):
	global accountNamesList, accountBalancesListm accountPasswordsList
	print('Account', accountNumber)
	print('		Name:', accountNamesList[accountNumber])
	print('		Balance:', accountBalancesList[accountNumber])
	print('		Password:', accountPasswordsList[accountNumber])
	print()

def getBalance(accountNumber, password):
	global accountNamesList, accountBalancesList, accountPasswordsList
	if password != accountPasswordsList[accountNumber]:
		print('Incorrect password')
		return None
	return accountBalancesList[accountNumber]


# --- snipped additional functions ---

# Create two sample accounts

print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:" len(accountNamesList))
newAccount("Mary", 12345, 'nuts')

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

# --- snipped additional user interface ---

print('Done')
