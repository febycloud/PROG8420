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
#using dyanamic programming to find likehood
def likeHood(n):
	#find range to dice and sumtotal
	dp=[[0 for _ in range(6*n+1)]for _ in range(n+1)]
	for i in range(1,7):
		dp[1][i]=1
	for i in range(2,n+1):
		for j in range(i,i*6+1):
			for k in range(1,7):
				if j>=k+1:
					#dp formula
					dp[i][j]+=dp[i-1][j-k]
	res={}
	#add value to dict
	for i in range(n,n*6+1):
		res.update({i:dp[n][i]*1.00/6**n})
	return res

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
	errp={}
	for i in key:
		errp.update({i:count[i]/int(rolls)}) 
	print('the total appear percentage is :')
	print(count)
	#calculate likelyhood of dices
	likehood=likeHood(dice)
	print('likehood value is: ')
	print(likehood)
	#calculate percentage error of each total
	error={}
	for i in key:
		errorp=errp[i]-likehood[i]
		error.update({i:errorp})
	print('error percentage is: ')
	print(error)
	
	#run the module
diceRoll()