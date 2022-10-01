import glob

files = glob.glob('./*.md')
print(files)
for fi in files:
	f=open(fi,'r')
	text = f.readlines()
	f.close()
	
	str = ""
	
	for line in text:
		tmp = line
		tmp = tmp.replace('a','i')
		tmp = tmp.replace('e','i')
		tmp = tmp.replace('o','i')
		tmp = tmp.replace('u','i')
		str += tmp
	
	print(str)
	
	f=open(fi,'w')
	f.write(str)
	f.close()