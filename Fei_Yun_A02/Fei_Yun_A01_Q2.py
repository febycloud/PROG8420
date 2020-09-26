#The Course:PROG8420
#Assignment No:2
#Create date:2020/09/25
#Name: Fei Yun

location1=input('put the txt file with .py same folder and input file name: ')
def wordCount(location):
	file=open(location,"r")
	wordcount={}
	#split word and lower all words
	Text=file.read().lower().split()
	#clean -,.\n special characaters
	for char in '-.,\n':
		Text=[item.replace(char,'') for item in Text]
		#count word
	for word in Text:
		#creat word if not exist
		if word not in wordcount:
			wordcount[word]=1
		else:
			#count +1 if exist
			wordcount[word]+=1
			#sort word as alpha order
	for k in sorted(wordcount):
		print("%s  : %d" %(k,wordcount[k]))
	file.close()	

wordCount(location1)
