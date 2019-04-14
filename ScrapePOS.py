"""Elementary script to parse Wiki articles and POS tag it"""

import sys
import requests
import urllib
from urllib.request import urlopen
from requests import get
from bs4 import BeautifulSoup as bs
import urllib.parse
import spacy

search_term = str(sys.argv[1])
search_term = urllib.parse.quote(search_term, safe='/', encoding=None, errors=None)
page = urlopen("https://en.wikipedia.org/wiki/" + search_term)
soup = bs(page, 'html.parser')
text = ''

print()
print('===================')
print('ARTICLE')
print('===================')

for p in soup.find_all('p'):
	text += p.get_text()

print(text)

nlp = spacy.load('en_core_web_sm')
text = nlp(text)

print()
print('===================')
print('POS Tagging')
print('===================')
print()

for token in text:
	print(token.text, token.pos_)




