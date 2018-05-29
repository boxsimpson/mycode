#!/usr/bin/env python3

#Illustrated By Lashawn Simpson

vcolor = ['Red','Blue','Green']  #Valid Colors
novcolor = ['Purple','Orange','Yellow'] #Invalid colors
odd = [1,3,5,7,9]
even =  [0,2,4,6,8]
shape = ['Circle','Square','Triangle']

print("Enter a color... " )
input()
if vcolor: ## Refering to valid colors
	print(" You picked a primary color!! ")
else: ## Refering to invalid colors
	print(" You did not pick a primary color! ")

print("Enter a number... " )
input()
if odd: #Odd number selection
	print( " You have chosen a odd number!!" )
else: #Even number selection
	print(" You have chosen a even number!!" ) 

print("Enter a shape... " )
input()
if shape: # refering to Circle Square or Triangle
	print(" Good Choice, I would have picked this also!! " )
else:
	print("Hmmm i didnt expect that one" )

#Cant get this to work how I want and im not sure why



