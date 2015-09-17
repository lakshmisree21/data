import webbrowser,os,sys,requests,bs4
res = requests.get("http://www.vegrecipesofindia.com/recipes/indian-breakfast-recipes/")
type(res)
res.status_code == requests.codes.ok
try: 
	res.raise_for_status()
except Exception as exc:
	print("there is a problem: %s" % (exc))	
soup = bs4.BeautifulSoup(res.text)
search = soup.select(".entry-title a")
sample = {}
y=min(3,len(search))
for i in range(y):
	webbrowser.open(search[i].get("href"))
	a = search[i].get("href")
	x = requests.get(a)
	type(x)
	print "hello"
	x.status_code = requests.codes.ok
	print x
	#www.vegrecipesofindia.com/recipes/indian-breakfast-recipes/http://www.vegrecipesofindia.com/oats-upma-recipe/
	try:
		x.raise_for_status()
	except Exception as exc:
		print("there is problem %s" % (exc))
	l = bs4.BeautifulSoup(x.text)
#	sample["heading"]= soup.select(".entry_header ")
#	print sample
#	examplefile = open("example.text","wb")
#	examplefile.write(search[0].get("href"))
#	examplefile.close()	
	sample = soup.select(".entry-header")	
	if sample == []: 
	    print "nothing"
	else:
		sample1 = sample[i].get("text")
		print "loading"		
		m = requests.get(sample1)
		m.raise_for_staus()
		myfile = open("recipe","wb")
		for chunk in m.iter_content(10000):
				myfile.write(chunk)
		myfile.close()		
	print "done"
