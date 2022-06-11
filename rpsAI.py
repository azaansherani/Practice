# import random
from random import randint
print("\n********Rock********\n********Paper********\n********Scissors********\n")

player_wins = 0
comp_wins = 0

while player_wins<2 and comp_wins<2:
	print(f"\nPlayer's Score = {player_wins}; Computer's score = {comp_wins}")
	player = input("Player, make your move : ").lower()
	ran_num = randint(0,2)
	if ran_num==0:
		computer="rock"
	elif ran_num ==1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"\nComputer plays {computer}")

	if player:	
		if (player=="rock" or player=="paper" or player=="scissors"):
			if player=="rock" and computer=="scissors":
				print("\nPlayer wins\n Way to go Gamer!\n")
				player_wins += 1
			elif player=="scissors" and computer=="paper":
				print("\nPlayer wins\n Way to go Gamer!\n")
				player_wins += 1
			elif player=="paper" and computer=="rock":
				print("\nPlayer wins\n Way to go Gamer!\n")
				player_wins += 1
			elif computer=="rock" and player=="scissors":
				print("\nComputer wins\n NOOB LMAO!\n")
				comp_wins += 1
			elif computer=="scissors" and player=="paper":
				print("\nComputer wins\n NOOB LMAO\n")
				comp_wins += 1
			elif computer=="paper" and player=="rock":
				print("\nComputer wins\n NOOB LMAO!\n")
				comp_wins += 1 
			elif player==computer:
				print("\nIt's a TIE, I see you're as smart as a Computer.\n")
			
		else:
			print("\nWrong entry! Your whacky ass ain't a Gamer.\n ")
	else:
		print("\n NO ENTRY LOSER!\n")


print(f"\nFinal Score\nPlayer's Score = {player_wins}; Computer's score = {comp_wins}\n")











