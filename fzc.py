import requests
from bs4 import BeautifulSoup

t = "https://twitter.com/kdxn"

r = requests.get(t)

sp = BeautifulSoup(r.text, "html.parser")
print(sp.title.string)

#print(r.text)
print(r.status_code)
