from omdbapi import *
import pickle
import random
 
def generate_trigram(words):
    if len(words) < 3:
        return
    for i in xrange(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])

def generate_chain(plot_list):
	chain = {}
	 
	for line in plot_list:
	    words = line.split()
	    for word1, word2, word3 in generate_trigram(words):
	        key = (word1, word2)
	        if key in chain:
	            chain[key].append(word3)
	        else:
	            chain[key] = [word3]
	 
	pickle.dump(chain, open("chain.p", "wb" ))

def generate_plot():
	chain = pickle.load(open("chain.p", "rb"))
 
	new_plot = []
	sword1 = "BEGIN"
	sword2 = "NOW"
	 
	while True:
	    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
	    if sword2 == "END":
	        break
	    new_plot.append(sword2)
	 
	return ' '.join(new_plot)