import requests,os,sys,bs4
url = "http://www.simplyrecipes.com"
#os.makedirs("recipepic",1)
res = requests.get(url)
res.raise_for_status()
#os.mkdir(mydir)
exfile = open("/home/dell/Desktop/DATA/recipepic/"+"example.html","wb")
for chunk in res.iter_content(10000):
	exfile.write(chunk)
exfile.close()
soup = bs4.BeautifulSoup(res.text)
recipe = soup.select("div .featured-image img")

i=0
for i in range (len(recipe)):
	if recipe == []:
		print " There is nothing"
	else:
		recelm = recipe[i].get("src")
		#res = requests.get(recelm)
		#res.raise_for_status()
		print "downloading"
	#	downloadurl(recelm):
#def downloadurl(rec):	
		res = requests.get(recelm)
		res.raise_for_status()
		imagefile = open(os.path.join("recipepic",os.path.basename(recelm)),'wb')
		for chunk in res.iter_content(10000):
			imagefile.write(chunk)
		imagefile.close()
		i+=1

	#featured-image
