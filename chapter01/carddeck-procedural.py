# Carddeck 
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

startingDeckList = []
for suit in SUIT_TUPLE:
	for thisValue, rank in enumerate(RANK_TUPLE):
		cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
		startingDeckList.append(cardDict)

print(startingDeckList)