from omdbapi import *
import pickle
import random
 
def generate_ordergram(words, order):
    if len(words) < order:
        return
    for i in xrange(len(words) - (order - 1)):
        yield tuple([words[i+x] for x in xrange(0,order)])

def generate_chain(plot_list, order):
	chain = {}
	 
	for plot in plot_list:
	    words = plot.split()

	    for x in generate_ordergram(words,order):
	    	key = x[:order-1]
	    	if key in chain:
	    		chain[key].append(x[-1])
	    	else:
	    		chain[key] = [x[-1]]
	 
	pickle.dump(chain, open("chain{}.p".format(order), "wb" ))

def generate_plot(order):
	chain = pickle.load(open("chain{}.p".format(order), "rb"))
	
	start_words = []
	for x in xrange(order-1):
		start_words.append("BEGIN{}".format(x))

	new_plot = []
	while True:
		generated_word = random.choice(chain[tuple(start_words[:])])
		for x in xrange(order-2):
			start_words[x] = start_words[x+1]
		start_words[-1] = generated_word
		if start_words[-1] == "END":
			break
		new_plot.append(start_words[-1])

	return ' '.join(new_plot)

def generate_pickles(movie_data, min_order, max_order):
	for x in xrange(min_order,max_order+1):
		plot_list = get_movie_plots(movie_data,x)
		chain = generate_chain(plot_list,x)

#generate_pickles('chain1000.p', MIN_ORDER, MAX_ORDER)