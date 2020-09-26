#The Course:PROG8420
#Assignment No:2
#Create date:2020/09/25
#Name: Fei Yun

import math
import random
import pandas
from collections import Counter

#random simulate the dice would be appear
def Dice(num):
	min=num
	max=num*6
	return random.randint(min,max)


def diceRoll():
	#receiver user input
	strd=input('input number of dice: ')
	try:
		dice=int(strd)
		if dice>16:
			print('max support 16 dices')
	except ValueError:
		print('invaild value')
		
	strn=input('input rolls of dice: ')
	try:
		rolls=int(strn)
		if rolls<1:
			print('rolls should be over than 1')
	except ValueError:
		print('invaild value')
	numbers=[]
	#simulate rolls dices
	for i in range(0,rolls):
		numbers.append(Dice(dice))	
	#count total appears
	count=Counter(numbers)	
	#get total appears list
	key=list(count.keys())
	print('the total appear percentage is :')
	print(count)
	#calculate likelyhood of dices
	likehood=7*dice	/2
	print('likehood value is: ')
	print(likehood)
	#calculate percentage error of each total
	error=[]
	for i in key:
		error.append((i-likehood)/likehood)
	print('error percentage is: ')
	print(error)
	
	#run the module
diceRoll()