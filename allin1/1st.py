#http://food.ndtv.com/recipes/indian-recipes
import webbrowser,sys,requests,bs4
res = requests.get("http://www.vegrecipesofindia.com/recipes/indian-breakfast-recipes/")
type(res)
res.status_code == requests.codes.ok
try: 
	res.raise_for_status()
except Exception as exc:
	print("there is a problem: %s" % (exc))	
soup = bs4.BeautifulSoup(res.text)
search = soup.select(".entry-title a")
y=min(3,len(search))
for i in range(y):
	webbrowser.open(search[i].get("href"))
