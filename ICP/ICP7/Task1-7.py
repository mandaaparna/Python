import requests as rq
from bs4 import BeautifulSoup

response=rq.get("https://en.wikipedia.org/wiki/Google")
cont=BeautifulSoup(response.content,"html.parser")
print(cont.text)
f=open("input.txt", "w+",encoding="utf-8")
f.write(cont.text)
f.close()