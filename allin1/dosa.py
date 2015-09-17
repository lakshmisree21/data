import os,sys,requests,bs4
url = "http://www.vegrecipesofindia.com/oats-dosa-recipe/"
token = url.split('/')
'/'.join(token[:-1])
dirnew = os.path.join("/home/dell/Desktop/DATA/"+token[3])
if os.path.exists(dirnew)== True:
	{}
else:
	os.makedirs(token[3],1)
res = requests.get(url)
res.raise_for_status()
print dirnew
recipefile = open(dirnew+"/"+token[3]+".html","wb")
print recipefile
for chunk in  res.iter_content(10000):
	recipefile.write(chunk)
recipefile.close()
soup = bs4.BeautifulSoup(res.text)
image = soup.select("div .entry-content img")
if image == []:
	print"empty"
else:
	imagefile = image[0].get("src")
	res = requests.get(imagefile)
	res.raise_for_status()
	recipefile = open(dirnew + "/" + token[3]+".jpg","wb")
	for chunk in res.iter_content():
		recipefile.write(chunk)
	recipefile.close()
recipefile= open(dirnew+"/"+token[3]+".text","wb")
recipefile.close()
recipefile = open(dirnew+"/"+token[3]+".text","a")
title = soup.select("div .ERSName")
recipefile.write("Recipe :\n"+title[0].getText().encode("UTF")+"\n\n")
ingredient = soup.select("div .ERSIngredients")
for chunk in range (len(ingredient)):
	recipefile.write('/n')

	recipefile.write( '\n'+ingredient[chunk].getText().encode("UTF")+'\n')
	recipefile.write("\n")	
instructions = soup.select("div .ERSInstructions")
for i in range (len(instructions)):
	recipefile.write(instructions[i].getText().encode("UTF")+'\n')
recipefile.close()	