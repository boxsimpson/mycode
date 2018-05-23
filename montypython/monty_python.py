#!/usr/bin/env python3
# illustrated by Lashawn Simpson

round = 0
while(True):
	round = round + 1
print('Finish the movie title, "Monty Python\'s The Life of ______"')
answer = input()
if (answer == 'Brian'):
	print('Correct')
	break

elif(round==3):
	print('Sorry, the answer was Brian.')
	break

else:
	print("sorry! Try again!")