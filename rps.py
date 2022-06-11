print("\n********Rock********\n********Paper********\n********Scissors********\n")
player_1 = input("Player 1 enter choice : ")
player_2 = input("Player 2 enter choice : ")
if player_1 and player_2:	
	if (player_1=="Rock" or player_1=="Paper" or player_1=="Scissors") and (player_2=="Rock" or player_2=="Paper" or player_2=="Scissors"):
		if player_1=="Rock" and player_2=="Scissors":
			print("\nPlayer 1 wins\n Way to go Gamer!\n")
		elif player_1=="Scissors" and player_2=="Paper":
			print("\nPlayer 1 wins\n Way to go Gamer!\n")
		elif player_1=="Paper" and player_2=="Rock":
			print("\nPlayer 1 wins\n Way to go Gamer!\n")
		elif player_2=="Rock" and player_1=="Scissors":
			print("\nPlayer 2 wins\n Way to go Gamer!\n")
		elif player_2=="Scissors" and player_1=="Paper":
			print("\nPlayer 2 wins\n Way to go Gamer!\n")
		elif player_2=="Paper" and player_1=="Rock":
			print("\nPlayer 2 wins\n Way to go Gamer!\n") 
		elif player_1==player_2:
			print("\nTIE\n")
		
	else:
		print("\nWrong entry! Your whacky ass ain't a Gamer.\n ")
else:
	print("\n NO ENTRY LOSER!\n")