#PROG8420
#Assignment05
#Fei Yun
#8680643
#create at 2020/11/18



#!/usr/bin/env python3

import numpy as np

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
		if dice>8:
			print('max support 8 dices')
	except ValueError:
		print('invaild value')
		
	strn=input('input rolls of dice: ')
	try:
		rolls=int(strn)
		if rolls<1:
			print('rolls should be over than 1')
	except ValueError:
		print('invaild value')
	#use numpy to simulate array
	result=np.random.randint(1,7,(dice,rolls))
	print("the simulation result is :")
	print(result)
	#sum up arraysvertical axis by numpy
	numbers=np.sum(result,axis=0)
	#count frequncy via numpy
	key,counts=np.unique(numbers,return_counts=True)
	count=dict(zip(key,counts))
	#calculate error
	errp={}
	for i in key:
		errp.update({i:count[i]/int(rolls)}) 
	print('the total appear percentage is :')
	print(count)
	likehood=likeHood(dice)
	print('likehood value is: ')
	print(likehood)
	#calculate percentage error of each total
	error={}
	print(key)
	for i in key:
		errorp=errp[i]-likehood[i]
		error.update({i:errorp})
	print('error percentage is: ')
	print(error)
	

diceRoll()
	