import random
print('welcome to the Rock Paper Scissors!')
print('This game is created by Dev Nirwal')
print('Choose how you wanna play:  ')
print('       Single player       or       Multiplayer player')
game_mode = input(' Type Single / Multi : ').lower()
print('Lets get started')
print('You will have 3 choices here')
print('# # # Rock # # #')
print('# # # Paper # # #')
print('# # # Scissors # # #')
game_continue = 'y'
while game_continue == 'y':
	if(game_mode == 'single'):
		print('Welcome to the single player mode . Here you will be fighting with computer')
		randm_no = random.randint(1,3)
		if(randm_no == 1):
			computer_input = 'rock'
		elif(randm_no == 2):
			computer_input = 'paper'
		else:
			computer_input = 'scissors'
		user_input = input('Input your move Rock / Paper / Scissors : ').lower()
		if(user_input == computer_input):
			print('This is a tie. ')
			print(f'The computer input is {computer_input}')
		elif(user_input == 'rock'):
			if(computer_input == 'paper'):
				print(f'You Lose ! The computer played {computer_input}')
			else:
				print(f"You win ! The compuer played {computer_input}")
		elif(user_input == 'paper'):
			if(computer_input == 'scissors'):
				print(f'You Lose ! The computer played {computer_input}')
			else:
				print(f'You win ! The compuer played {computer_input}')
		elif(user_input == 'scissors'):
			if(computer_input == 'paper'):
				print(f'You Lose ! The compuer played {computer_input}')
			else:
				print(f'You win ! The compuer played {computer_input}')
		else: 
			print('please try again')
	elif(game_mode == 'multi'):
	    player1 = input('Enter your  Player1 input Rock / Paper / Scissors : ').lower()
	    for i in range(1,20):
	        print('        N o             C h e a t i n g                 ')
	    player2 = input('Enter your  Player2 input Rock / Paper / Scissors : ').lower()        
	    if(player1 == player2):
	       	print('This is a tie ! Both played same move  ')                
	    elif(player1 == 'rock'):
	        if(player2 == 'scissors'):
	            print('Congratulation ! Player1 wins')
	        elif(player2 == 'paper'):	
	            print('Congratulation ! Player2 wins')
	        else:
	      	    print('Wrong input ! Try again')	
	    elif(player1 == 'paper'):
	        if(player2 == 'rock'):
	            print('Congratulation ! Player1 wins')
	        elif(player2 == 'scissors'):
	            print('Congratulation ! Player2 wins')
	        else:
	            print('Wrong Input try again !    ')
	    elif(player1 == 'scissors'):
	        if(player2 == 'paper' ):
	            print('Congratulation ! Player1 wins')	
	        elif(player2 == 'rock'):
	            print('Congratulation ! Player2 wins')	
	        else:
	            print('Wrong input ! Try again')
	    else:
	    	print('Wrong input!')
	user_input = input('Do you wanna play more? (y/n)').lower()
	if(user_input == 'n'):
		break	   		         
print('Thanks for playing thi game')    
print('Bye! Have a great time')	









