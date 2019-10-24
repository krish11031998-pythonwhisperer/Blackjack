import tkinter
import random

card = []
dealer_cards = []
player_cards = []

def _load_image(card_images):
	suits = ['heart','club','diamond','spade']
	face_cards=  ['jack','queen','king']
	extension = "ppm"
	for suit in suits:
		for number in range(1,11):
			name = "cards/{0}_{1}.{2}".format(str(number),suit,extension)
			image = tkinter.PhotoImage(file=name)
			card_images.append((number,image))

	for suit in suits:
		for face in face_cards:
			name = "cards/{0}_{1}.{2}".format(face,suit,extension)
			image = tkinter.PhotoImage(file=name)
			card_images.append((10,image))

def _deal_cards(y):
	if y == 'Dealer':
		frame = dealer_card_frame
	elif y == 'Player':
		frame = player_card_frame
	next_card = deck.pop(0)
	tkinter.Label(frame,image=next_card[1],relief="raised").pack(side='left')
	return next_card[0]

def _score_hand(hand):
	score = 0
	ace = False
	for card in hand:
		if card == 1 and ace==False:
			ace = True
			score+=11
		score +=card
		if score>21 and ace==True:
			score -=10
	return score

def _deal_dealer():
	global dealer_card_value
	global result_string
	global dealer_score
	if dealer_score <= 17:
		dealer_cards.append(_deal_cards('Dealer'))
		dealer_score = _score_hand(dealer_cards)
		print(dealer_cards)
		dealer_card_value.set(dealer_score)
		player_score = _score_hand(player_cards)
		if dealer_score >21:
			result_string.set('Player Wins!!!')
		elif dealer_score == 21:
			result_string.set('Dealer Wins , BLACKJACK!')
		elif dealer_score <21 and dealer_score < player_score:
			result_string.set('Player Wins!!')
		elif dealer_score < 21 and dealer_score > player_score:
			result_string.set('Dealer Wins!!')
		elif dealer_score == player_score:
			result_string.set('The Game was drawn')

def _deal_player():
	global player_card_value
	global result_string
	player_cards.append(_deal_cards('Player'))
	player_score = _score_hand(player_cards)
	dealer_score = _score_hand(dealer_cards)
	player_card_value.set(player_score)
	if player_score >21:
		result_string.set('Dealer Wins!!!')
	elif player_score == 21:
		result_string.set('Player Wins , BLACKJACK!')
	elif player_score < 21 and player_score>dealer_score:
		result_string.set('Player Wins!')
	elif player_score <21 and player_score<dealer_score:
		result_string.set('Dealer Wins!')
	elif player_score == dealer_score:
		result_string.set('The Game is drawn!')

def _calculate_value(a, b):
	value = 0
	if (b[0]>0) and (b[0]<10):
		value += b[0]
		if a=='Dealer':
			dealer_card_value.set(value)
		elif b =='Player':
			player_card_value.set(value)
	elif b[0] == 10:
		value +=10
		if a=='Dealer':
			dealer_card_value.set(value)
		elif b =='Player':
			player_card_value.set(value)

def _dealer_cf():
	global dealer_label, dealer_card_value,dealer_score,dealer_ace,dealer_card_frame
	dealer_label = tkinter.Label(card_frame,text='Dealer',background='green',fg='white').grid(row=0,column=0,sticky ='n')
	dealer_card_value = tkinter.IntVar()
	dealer_score = 0
	dealer_ace = False
	dealer_card_value.set(0)
	dealer_card_value_label = tkinter.Label(card_frame,textvariable=dealer_card_value,background='green',fg='white').grid(row=0,column=0)
	# embedded frame to hold the dealers card
	dealer_card_frame = tkinter.Frame(card_frame,background='green')
	dealer_card_frame.grid(row=0,column=1,sticky='ew',columnspan=2)

def _player_cf():
	global player_label,player_card_value,player_score,player_ace,player_card_frame
	player_label = tkinter.Label(card_frame,text='Player',background='green',fg='white').grid(row=1,column=0,sticky='n')
	player_card_value = tkinter.IntVar()
	player_score = 0
	player_ace = False
	player_card_value.set(0)
	player_card_value_label = tkinter.Label(card_frame,textvariable=player_card_value,background='green',fg='white').grid(row=1,column=0)
	# embedded frame to hold the players card
	player_card_frame = tkinter.Frame(card_frame,background='green')
	player_card_frame.grid(row=1,column=1,sticky='ew',columnspan=2)

def _start_game():
	_deal_player()
	_deal_dealer()
	_deal_player()

def _reset_game():
	global deck,result_string
	result_string.set('BlackJack Time!!')
	dealer_cards.clear()
	player_cards.clear()
	player_card_frame.destroy()
	dealer_card_frame.destroy()
	_dealer_cf()
	_player_cf()
	_shuffle_card()
	_start_game()

def _shuffle_card():
	deck = list(cards)
	random.shuffle(deck)
def play():
	# dealer_cards
	# player_cards
	_start_game()
	mainWindow.mainloop()

mainWindow = tkinter.Tk()
mainWindow.title('Blackjack')
mainWindow.geometry('649x480')
mainWindow['padx'] = 10
mainWindow['pady'] = 10
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=10)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)

# Creating a result entry
result_string = tkinter.StringVar()
result_string.set('Blackjack Time!!!')
result = tkinter.Label(textvariable=result_string)
result.grid(row=0, column=1, sticky='nsew')


# Creating a Frame in the mainWindow for the cards to be drawn and displayed
card_frame = tkinter.Frame(mainWindow,background='green')
card_frame.grid(row=1,column=0,columnspan = 3,sticky='nsew')

card_frame.columnconfigure(0,weight=1)
card_frame.columnconfigure(1,weight=9)
card_frame.rowconfigure(0,weight=1)
card_frame.rowconfigure(1,weight=1)

# dealers labels
dealer_label = tkinter.Label(card_frame,text='Dealer',background='green',fg='white').grid(row=0,column=0,sticky ='n')
dealer_card_value = tkinter.IntVar()
dealer_score = 0
dealer_ace = False
dealer_card_value.set(0)
dealer_card_value_label = tkinter.Label(card_frame,textvariable=dealer_card_value,background='green',fg='white').grid(row=0,column=0)
# embedded frame to hold the dealers card
dealer_card_frame = tkinter.Frame(card_frame,background='green')
dealer_card_frame.grid(row=0,column=1,sticky='ew',columnspan=2)

# players labels
player_label = tkinter.Label(card_frame,text='Player',background='green',fg='white').grid(row=1,column=0,sticky='n')
player_card_value = tkinter.IntVar()
player_score = 0
player_ace = False
player_card_value.set(0)
player_card_value_label = tkinter.Label(card_frame,textvariable=player_card_value,background='green',fg='white').grid(row=1,column=0)

# embedded frame to hold the players card
player_card_frame = tkinter.Frame(card_frame,background='green')
player_card_frame.grid(row=1,column=1,sticky='ew',columnspan=2)


# creating the buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3,column=0,columnspan=3,sticky='nw')
dealer_button = tkinter.Button(button_frame, text='Dealer', command = _deal_dealer)
dealer_button.grid(row=0,column=0,sticky='nw')
player_button = tkinter.Button(button_frame, text='Player', command = _deal_player)
player_button.grid(row=0,column=1,sticky='e')
reset_button = tkinter.Button(button_frame, text='Reset', command= _reset_game)
reset_button.grid(row =0,column=2,sticky='e')
shuffle_button = tkinter.Button(button_frame, text='Shuffle', command= _shuffle_card)
shuffle_button.grid(row =0,column=3,sticky='e')


# CARD IMAGES LOADED
cards = []
_load_image(cards)
print(cards)

deck = list(cards)
random.shuffle(deck)
print(dealer_cards)
print(player_cards)

if __name__ == "__main__":
	play()