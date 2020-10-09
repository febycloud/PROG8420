import itertools
import random
def display_board(board):
	print(board['1']+"|"+board['2']+"|"+board['3'])
	print('-+-+-')
	print(board['4']+"|"+board['5']+"|"+board['6'])
	print('-+-+-')
	print(board['7']+"|"+board['8']+"|"+board['9'])
	

def player_input():
	player1=input('请输入你的棋子选择:(X or O)')
	while player1 not in ['X','O']:
		player1=input('请重新输入你的棋子选择:(X or O)')
	player2 = 'O' if player1 == 'X' else 'X'
	return player1,player2
	

def chooseFirst():
	turn=random.choice(['X','O'])
	print('\n'+turn+' go first!')
	return turn

def place_marker(correctInput,turn):#记录落子
	move=input('落子'+turn+'例如:1,2:')
	while move not in correctInput:
		print('\n重新输入落子:')
		move=input('\n落子'+turn+'e.g.1.2:')
	correctInput.remove(move)#remove() 函数用于移除列表中某个值的第一个匹配项。move是移除的对象
	return move

def board2magic(board):
	# 将棋盘位置转换为用三阶幻方同位置上数字表示
	tempBoard=board.copy()#字典的copy()方法相当于一种深复制，即将原本的字典dic1复制出一个内容一模一样的字典给另一个字典变量dic2，dic1和dic2的内容完全相同，但内存地址不同，不是共享引用，其中任何一方做出改变，另外一方不受影响
	magic3=[4,9,2,3,5,7,8,1,6]
	j=0
	print(tempBoard.items())
	for i in list(tempBoard.keys()):#keys()返回一个字典所有的键。调用list()返回列表值。
		tempBoard[str(magic3[j])]
		#str()对象转化为适于人阅读的形式,返回string.可以将非字符串类型转换成字符串；
		#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值,列表从零计数
		j=j+1
	print(tempBoard.items())
	return tempBoard

#sum() 方法对系列进行求和计算。sum(iterable[, start])iterable -- 可迭代对象，如：列表、元组、集合。
#start -- 指定相加的参数，如果没有设置这个值，默认为0。
#combinations(iterable, r):
#创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序:
def checkWin_sub(pieces):
	comb = list(itertools.combinations(pieces, 3))
	print('comb is ',comb)
	isWin = True if 15 in [sum(i) for i in comb] else False
	return isWin

#Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
#语法：
#dict.items()
#返回可遍历的(键, 值) 元组数组。
def checkWin(board):
	# 判断是否有获胜方
	tempBoard = board2magic(board)
	Xpieces = [int(x[0]) for x in tempBoard.items() if 'X' in x[1]]
	print('Xpices is ',Xpieces)
	Opieces = [int(d[0]) for d in tempBoard.items() if 'O' in d[1]]
	Xwin = checkWin_sub(Xpieces)
	Owin = checkWin_sub(Opieces)
	winner = 'N'
	if Xwin == True:
		winner = 'X'
	elif Owin == True:
		winner = 'O'
	return winner

def main():
	while True:
		theBoard={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
		correctInput=list(theBoard.keys())
		player1, player2 = player_input()
		turn=chooseFirst()
		for rounds in range(9):
			display_board(theBoard)
			move=place_marker(correctInput,turn)
			theBoard[move]=turn
			turn='O' if turn=='X' else 'X'
			winner=checkWin(theBoard)
			if winner=='N':
				if rounds==8:
					print('\nDraw')
			else:
				print("\n'"+winner+"'wins!")
				break
		display_board(theBoard)
		if input('按"y"键再来一盘游戏，其他键则结束游戏') != 'y':
			break
main()