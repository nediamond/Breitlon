import requests
from bs4 import BeautifulSoup
from random import shuffle
from pprint import pprint as pp
import json

def get_article_list():
	# Scraping Salon

	html = requests.get("http://www.salon.com/").text
	soup = BeautifulSoup(html, "html.parser")

	articles = soup.find_all(class_="latest-link") + soup.find_all(class_="card-article")
	sal_article_data = []
	for article in articles:
		author = getattr(article.find(class_="writer"),'text', '')
		title = article.text.strip()
		if not title: continue
		if author: title = title.replace(author, '').strip()
		link = (article.find('a') or article)['href']
		sal_article_data.append((title, author, link))
			
			
	# Scraping Breitbart

	html = requests.get("http://www.breitbart.com/").text
	soup = BeautifulSoup(html, "html.parser")

	# Main Articles
	articles = soup.find_all('article')
	breit_article_data =[]
	for article in articles:
		byline = article.find('address')
		byline = byline['data-aname'].title() if byline else ''
		link = article.find('a')
		title = link.text if link.text else article.find('footer').text
		try:
			breit_article_data.append((title, byline, "http://www.breitbart.com"+link['href']))
		except KeyError:
			continue
		
	sarts = map(lambda x: x+('s',), sal_article_data)
	barts = map(lambda x: x+('bb',), breit_article_data)

	return join_lists(barts, sarts)

	
# Splices lists together until one list runs out	
def join_lists(l1, l2):
	new_list = []
	for i in range(max(len(l1), len(l2))):
		try:
			new_list.append(l1[i])
		except IndexError:
			break
			
		try:
			new_list.append(l2[i])
		except IndexError:
			break
			
	return new_list
		
	
	
	
	
