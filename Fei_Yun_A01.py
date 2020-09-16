#The Course:PROG8420
#Assignment No:1
#Create date:2020/09/16
#Name: Fei Yun

#Write a module that prompts the user for an integer and then 
#returns the factorial of that integer

#import math method
import math


#define a function for accept input and return factorial number
def givefactorial(str):
	#try convert string to int
	try:
		num=int(str)
	#if cannot convert return an error
	except ValueError:
		return 'the value is not integer'
	#otherwise return factorial number
	return math.factorial(num)

#assignment 1-1 part
input_str=input('please input a number: ')
print(givefactorial(input_str))
						
						
			
#Write a module that gets a sequence of integers from the user,
#and, whencomplete, displays a report showing the sum, 
#number of integers entered and anaverage.


#define accept user input numbers
def getnums():
	#create a list
	nums=[]
	#set loop triger
	triger=True
	#when triger is true let user input number
	while triger==True:
		str=input('please input a number: ')
		# if user input nothing quit loop
		if str == '' or str== '\\r':
			triger=False
			print('all number added')
			return nums
		else:
			try:
				#if user input a number, add to list
				num=int(str)
				nums.append(num)
				print('value added')
			except ValueError:
				#if user input something else,refuse and notify
				print('Invalid Entry! input is not integer')
	return nums

def show(nums):
	# if user input nothing return nothing
	if len(nums)==0:
		print('no numbers')
	else:
		#show sum 
		print('the sum is ',sum(nums))
		#show number count
		print('the number of integers is ',len(nums))
		#show avh value
		print('the avg of numbers is',sum(nums)/len(nums))	

#assignment 1-2 part		
number=getnums()
show(number)


			
			
	