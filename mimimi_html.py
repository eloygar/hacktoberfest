import glob
import requests
from bs4 import BeautifulSoup

files = glob.glob('./*.html')
print(files)
for fi in files:
	f=open(fi,'r',encoding='utf-8')
	text = f.readlines()
	f.close()
	
	s = ""
	for line in text:
		s += line	
	
	soup = BeautifulSoup(s, 'html.parser')

	for e in soup.find_all(text=True):
		e.string.replace_with(e.string.
		replace('a','i').
		replace('e','i').
		replace('o','i').
		replace('u','i').
		replace('á','í').
		replace('é','í').
		replace('ó','í').
		replace('ú','í'))

	s = str(soup).split("\n",1)[1]
	
	f=open(fi,'w',encoding='utf-8')
	f.write(s)
	f.close()