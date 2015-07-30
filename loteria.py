import random
import os

from flask import (
	Flask,
	request, session,
	url_for, render_template, redirect
)

# Create a Flask application object
app = Flask(__name__)

# SEssion variables are sorerdt client-side (on the user0s browser).
# The content of these variables si encryted, so users can't actually
# read thir contents, They could edit the seasson data, but because it
# would not be signed with the secret key below, the server would
# reject is as invalid.
# you neet to set a secret key (random txt) and keep it secret!
app.secret_key = "qwerty"
# The path to the directory containing our images
# We will store a list of image files names in a session variable.
IMAGE_DIR = app.static_folder

#######################
### Helper funtions ###
######################
def init_game():
	# initialize a new deck (a list of filenames)
	image_names = os.listdir(IMAGE_DIR)
	# shuffle the deck
	random.shuffle(image_names)
	# store it n the user0s session
	# 'session' is a special global object that flask provides 
	#which exposes the basic session management funcionality
	session['images'] = image_names

def select_from_deck():
	try:
		image_name = session['images'].pop()
	except IndexError:
		return None #sentinel
	return image_name

#######################
### View functions ###
######################
@app.route('/')
def index():
	init_game()	
	return render_template("index.html")


@app.route('/draw')
def draw_card():
	image_name = select_from_deck()
	if image_name is None:
		return render_template("Game Over.html")
	return render_template("showcard.html", image_name = image_name)



if __name__ == "__main__":
    app.run(debug = True)