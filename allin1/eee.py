import webbrowser,requests,bs4,sys
res = requests.get("https://www.google.com/search?q=Iamfeelinglucky")
type(res)
res.status_code == requests.codes.ok
print res
try: 
	res.raise_for_status()
except Exception as exc:
	print("there is a problem: %s" % (exc))	
soup = bs4.BeautifulSoup(res.text)
example=soup.select('.r a')
numopen = min(5,len(example))
for i in range(numopen):
	webbrowser.open('http://google.com'+example[i].get('href'))