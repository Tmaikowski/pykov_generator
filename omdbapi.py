import requests
import pickle

MIN_ORDER = 2
MAX_ORDER = 5

def get_movie_plots(movie_pickle, order):
	movie_list = pickle.load(open(movie_pickle,'rb'))

	starting_words = ""
	for x in xrange(order-1):
		starting_words += "BEGIN{} ".format(x)
	movie_plots = []
	for movie in movie_list:
		try:
			resp = requests.get('http://www.omdbapi.com/?t={}&plot=full&r=json'.format(movie))
			if resp.json()['Response'] == "True":
				plot = resp.json()['Plot']
				movie_plots.append(starting_words + plot + " END")
		except:
			pass
	return movie_plots