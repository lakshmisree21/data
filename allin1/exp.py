import webbrowser,sys,requests,bs4

#if len(sys.argv)>1:
		#for arg in sys.argv:
			#{
#			address = ' '.join(sys.argv[1:])
#			webbrowser.open("http://food.ndtv.com/recipes/indian-recipes"+address)
			#}	
			#res = requests.get("http://food.ndtv.com/recipes/indian-recipes"+address)
			#type(res)
		#	res.status_code=requests.codes.ok
			#len(res.text)
			#res.raise_for_status()
			#playfile = open("example.txt","wb")
			#for i in res.iter_content(100000):
			#	playfile.write(i)
			#playfile.close()
#			sample = bs4.BeautifulSoup(res.text)
#			type(sample)
examplefile = open('exam.html')
examplesoup =bs4.BeautifulSoup(examplefile.read())
elems =  examplesoup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str (elems[0])
elems[0].attrs