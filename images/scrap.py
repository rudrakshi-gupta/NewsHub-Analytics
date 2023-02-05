import csv
from bs4 import BeautifulSoup
import requests

baseurl = "https://www.noon.com/egypt-en"
headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

links = []
for c in range(1,65):
    r = requests.get('https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page='+str(c)+'&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc',headers=headers)

    soup = BeautifulSoup(r.content,'html.parser')
    plist = soup.findAll('span', class_="productContainer")
    # print(plist)
    for items in (plist):
        links.append(baseurl + items.a.get('href'))
print(len(links))

n = 8
num = 0
for i in range(n):
  for j in range(n):
    for k in range(n):
	    if(i+j+k == n):
		    num = num + 1
print(f"Total : {num}")