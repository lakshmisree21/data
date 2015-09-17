import os,sys,requests,bs4
url = "http://xkcd.com"
#os.makedirs('xkcd',1)
#while not url.endswith("#"):
print("downloading")
res =  requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
comicelem = soup.select("#comic img")
if comicelem == []:
	print("could not find the image")
else:
	print comicelem[0].get('src')
	comicurl = comicelem[0].get('src')
	print("downloading")
	res = requests.get("http:"+comicurl)	
	res.raise_for_status()
	imagefile = open(os.path.join('xkcd',os.path.basename(comicurl)),'wb')
	for chunk in res.iter_content(10000):
		imagefile.write(chunk)
	imagefile.close	