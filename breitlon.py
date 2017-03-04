import urllib
from bs4 import BeautifulSoup
from random import shuffle
from pprint import pprint as pp

# TODO: Combine the data from these lists into a single webpage called "Breitlon"

def get_article_list():
	# Scraping Salon

	html = urllib.urlopen("http://www.salon.com/").read()
	soup = BeautifulSoup(html, "html.parser")

	articles = soup.find_all('div', {'class':'story-info'})
	sal_article_data = []
	for article in articles:
		try:
			sal_article_data.append((article.a['title'], getattr(article.span.string,'strip',lambda: "")(), article.a['href']))
		except KeyError:
			continue
			
			
	# Scraping Breitbart

	html = urllib.urlopen("http://www.breitbart.com/").read()
	soup = BeautifulSoup(html, "html.parser")

	# Main Articles
	articles = soup.find_all('article')
	breit_article_data =[]
	for article in articles:
		try:
			breit_article_data.append((article.h2.a['title'], article.find('p', {'class':'byline'}).a.string, "http://www.breitbart.com"+article.h2.a['href']))
		except KeyError:
			continue
		
	# Trending Now
	trending_articles = soup.find('ul',{'id':'BBTrendUL'}).find_all('li')
	for article in trending_articles:
		breit_article_data.append((article.a['title'], "", article.a['href']))
		
		
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
		
	
	
	
	