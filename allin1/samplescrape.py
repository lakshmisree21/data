import bs4,requests,sys,os
url1 = "http://www.vegrecipesofindia.com/"
res = requests.get(url1)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
#selecting the pages
initial = soup.select(" .entry-header a")
j=0
for j in range (len(initial)):
	webp1 = initial[j].get("href")
	token = webp1.split("/")
	"./".join(token[:-1])
	dirnew = os.path.join("/home/dell/Desktop/DATA/allin1/"+token[3])
	if os.path.exists(dirnew)== True:
		{}
	else:
		os.makedirs(token[3],1)
	#downloading the html page
	webpdown = requests.get(webp1)
	webpdown.raise_for_status()
	pagesoup = bs4.BeautifulSoup(webpdown.text)
	recipefile = open(dirnew + "/" + token[3]+ ".html","wb")
	for chunk in webpdown.iter_content(10000):
		recipefile.write(chunk)
	recipefile.close()
#deleting the existing file
	recipefile=open(dirnew+"/"+token[3]+".text","wb")
	recipefile.close()
	recipefile=open(dirnew+"/"+token[3]+".text","a")
#heading
	content = pagesoup.select("div .ERSName")
	recipefile.write("Recipe : "+content[0].getText().encode("UTF")+"\n\n")
#ingredient
	content = pagesoup.select("div .ERSIngredients")
	recipefile.write(content[0].getText().encode("UTF")+"\n\n")
#instructions
	content = pagesoup.select("div .ERSInstructions")
	for i in range (len(content)):
		recipefile.write(content[i].getText().encode("UTF")+"\n\n")
	recipefile.close()
#image
	image = pagesoup.select("div .entry-content img")
	imageurl =image[0].get("src") 
	img = requests.get(imageurl)
	img.raise_for_status()
	recipefile = open(dirnew+"/"+token[3]+".jpg","wb")
	for i in img.iter_content(10000):
		recipefile.write(i)
	recipefile.close()
	j+=1