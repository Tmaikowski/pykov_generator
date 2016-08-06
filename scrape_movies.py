from bs4 import BeautifulSoup
import requests
import re
import pickle

movie_titles = []

def get_first_page_of_titles():
	resp1 = requests.get("http://www.listchallenges.com/top-1000-greatest-movies-of-all-time-by-imdb")
	get_titles(resp1,movie_titles)

def get_titles(resp, movie_titles):
	html_text = resp.text

	soup = BeautifulSoup(html_text, 'html.parser')

	div_titles = soup.find_all('div', class_='item-name')

	for title in div_titles:
		title_text = title.text
		clean_text = re.sub('\(.*\)', '', title_text)
		movie_titles.append(clean_text)

def get_remaining_titles():
	for page_num in xrange(2,15): #right number max is 26
		resp = requests.get("http://www.listchallenges.com/top-1000-greatest-movies-of-all-time-by-imdb/checklist/{}".format(page_num))
		get_titles(resp, movie_titles)

get_first_page_of_titles()
get_remaining_titles()

pickle.dump(movie_titles, open('chain1000.p','wb'))
