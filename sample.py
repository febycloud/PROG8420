import urllib.request
url='http://textfiles.com/adventure/aencounter.txt'
file = urllib.request.urlopen(url)
for line in file:
	url_line=line.decode()
	print(url_line)