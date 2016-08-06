from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from markov_multi import generate_plot, MIN_ORDER, MAX_ORDER

app = Flask(__name__)

@app.route('/')
def index():
	generated_orderplots = {}
	for x in xrange(MIN_ORDER,MAX_ORDER+1): #change back to xrange(2,6)
		generated_orderplots[x] = generate_plot(x)
	return render_template('index.html', generated_orderplots=generated_orderplots)

if __name__ == '__main__':
	app.run()