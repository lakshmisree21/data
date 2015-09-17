import os,sys,requests,bs4
url = "http://www.vegrecipesofindia.com/neer-dosa-recipe/"
newdir = "/home/dell/Desktop/DATA/neer-dosa-recipe/"
if os.path.exists(newdir) == True :
	print "already present"
else:
	os.makedirs("neer-dosa-recipe")
res = requests.get(url)
res.raise_for_status()
ex = open(newdir+"neer-dosa-recipe.html","wb")
for chunk in res.iter_content(10000):
	ex.write(chunk)
ex.close()	
soup = bs4.BeautifulSoup(res.text)
#image scraping

ex = soup.select("div .entry-content img")
if ex == []:
	print"no loading"
else:	
	image = ex[0].get("src")
	res = requests.get(image)
	res.raise_for_status()
	imagefile = open(os.path.join("neer-dosa-recipe",os.path.basename(image)),"wb")
	for chunk in res.iter_content(10000):
		imagefile.write(chunk)
	imagefile.close()
recfile = open(newdir+"neer-dosa-recipe.text","wb")	
recfile.close()
ex = soup.select("div .ERSName")
if ex == []:
	print "nothing"
else:
	#title = ex[0].getText().encode("UTF-8")
	#res = requests.get(title)
	#res.raise_for_status()
	#title = open(os.path.join("neer-dosa-recipe",os.path.basename(title)),"wb")
	#for chunk in res.iter_content(10000):
	#	title.write(chunk)
	#title.close()
	tittle = open(newdir+"neer-dosa-recipe.text","a")
	tittle.write("Recipe :\n"+ex[0].getText().encode("UTF-8")+"\n\n")
#tittle.write("\nIngredients:\n ")
ex = soup.select("div .ERSIngredients")
if ex== []:
	print "nothing"
else:
	i = 0
	for i in range(len(ex)):
		tittle.write("\n")
		tittle.write(ex[i].getText().encode("UTF-8"))
		tittle.write("\n")
		i+=1
ex = soup.select("div .ERSInstructions")
if ex == []:
	print "nothing"
else:
	i=0
	for i in range(len(ex)):
		tittle.write(ex[i].getText().encode("UTF-8"))	
		tittle.write("\n")			
		i+=1
tittle.close()
print "success"


