#The Course:PROG8420
#Assignment No:3
#Create date:2020/10/08
#Name: Fei Yun

#Quiz 1
import math
def Perfect(number):
	#check number from 2 to number
	for num in range(2,number):
		#result value
		sum=0
		#factor list
		factlist=[]
		#here we can search from 1 to sqrt(n) cuz if x is a factor of n ,it must be a n/x also is a factor
		for factor in range(1,int(math.sqrt(num))+1):
			#find all factors of num
			if num%factor==0:
				sum+=factor
				factlist.append(factor)
				factlist.append(num//factor)
				#the condition of n/x also have to be calculated 
				if factor>1 and num/factor!=factor:
					sum+=num/factor									
		if sum==num:
			print("perfect number is ",num)
			#remove num itself and 1
			factlist.remove(num)
			factlist.remove(1)
			print("its factors are ",sorted(factlist))
			print("")

Perfect(1000)

#Quiz 2
import random
import itertools

#make board
def display_board(board):
	print(board['1']+"|"+board['2']+"|"+board['3'])
	print('-+-+-')
	print(board['4']+"|"+board['5']+"|"+board['6'])
	print('-+-+-')
	print(board['7']+"|"+board['8']+"|"+board['9'])
	
#select player
def player():
	player1=input('please choose X or O : ')
	while player1 not in ['X','O']:
		player1=input('please choose X or O : ')
	player2='O' if player1=='X' else 'X'
	return player1,player2
#choose first turn to play
def chooseFirst():
	turn=random.choice(['X','O'])
	print(turn+' go first')
	return turn
#choose posistion to make 
def place_make(correctIn,turn):
	move=input(turn+' choose a position at 1,2,3....: ')
	#if postion is not avaliable
	while move not in correctIn:
		print('you cannot make there \n')
		move=input(turn+' choose a position at 1,2,3....: ')
	#delete avaliable position from list
	correctIn.remove(move)
	return move
	#change board to 3-layer magic square
	#magic square
	#4 9 2
	#3 5 7
	#8 1 6
	#all direction sum up to 15
	# this is the good way to judge if X or O win by just add their number up  
def borad2magic(board):
	temp=board.copy()
	magic=[4,9,2,3,5,7,8,1,6]
	j=0
	for i in list(temp.keys()):
		temp[str(magic[j])]
		j+=1
	return temp
	#check pieces win
def checkWin_sub(pieces):
	#check all pieces if sum up to 15
	comb=list(itertools.combinations(pieces,3))
	isWin=True if 15 in [sum(i) for i in comb] else False
	return isWin
	#check the game win
def checkWin(board):
	temp=borad2magic(board)
	#change X's keys to int
	Xpiece=[int(x[0]) for x in temp.items() if 'X' in x[1]]
	Opiece=[int(x[0]) for x in temp.items() if 'O' in x[1]]
	#check if X's keys can sum to 15
	Xwin=checkWin_sub(Xpiece)
	Owin=checkWin_sub(Opiece)
	winner='N'
	#result
	if Xwin==True:
		winner='X'
	elif Owin==True:
		winner='O'
	return winner
def TicTacToe():
	while True:
		gameBoard={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
		correctIn=list(gameBoard.keys())
		player1,player2=player()
		turn=chooseFirst()
		#start game in 9 steps
		for rounds in range(9):
			#display board
			display_board(gameBoard)
			#start move
			move=place_make(correctIn, turn)
			#next turn
			gameBoard[move]=turn
			turn='O' if turn=='X' else 'X'
			#check winner
			winner=checkWin(gameBoard)
			if winner=='N':
				if rounds==8:
					print('Draw')
			else:
				print(winner+' is winner')
				break
		display_board(gameBoard)
		#regame
		if input('press y to restart')!='y':
			break
TicTacToe()
			
	
