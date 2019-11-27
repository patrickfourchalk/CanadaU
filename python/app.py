"""
secret: OzcivV6aBZriJb7lFsU54QQJuUU
id:		wJhXch1ro-Dn0A
"""


import os

import praw
import prawcore
from flask import Flask, send_from_directory

# Create our Reddit client to communicate with Reddit
reddit = praw.Reddit(client_id='wJhXch1ro-Dn0A',
                     client_secret='OzcivV6aBZriJb7lFsU54QQJuUU',
                     user_agent='web:CanadaU:1.0 (by /u/rufhvbp)')

# Create our Flask application
app = Flask(__name__, static_folder='../react-app/build')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Add an endpoint to our Flask application
@app.route('/subreddit/<subreddit_id>')
def subreddit(subreddit_id):
	try:
		description = reddit.subreddit(subreddit_id).description_html
		return (description, 200)
	except prawcore.exceptions.NotFound:
		return ("Subreddit not found", 404)
	except prawcore.exceptions.Redirect:
		return ("Subreddit not found", 404)
		
# - - - WE WILL ADD NEW ENDPOINTS HERE - - -
@app.route('/subreddit/<subreddit_id>/subscribers')
def subscribers(subreddit_id):
	try:
		subs = str(reddit.subreddit(subreddit_id).subscribers)
		return (subs, 200)
	except prawcore.exceptions.Redirect:
		return ("Subreddit not found", 404)
	except prawcore.exceptions.NotFound:
		return ("Subreddit not found", 404)
		
@app.route('/subreddit/<subreddit_id>/banner_img')
def banner(subreddit_id):
	try:
		subs = reddit.subreddit(subreddit_id).banner_img
		return (subs, 200)
	except prawcore.exceptions.Redirect:
		return ("Subreddit not found", 404)
	except prawcore.exceptions.NotFound:
		return ("Subreddit not found", 404)
		
subredditIDs = ["uwaterloo", "UBC", "Uoft"]
		
@app.route('/subreddits')
def subreddits():
	subreddits = {};
	for subredditID in subredditIDs:
		subs = reddit.subreddit(subredditID)
		subreddits[subredditID] = {
			"display_name": subs.display_name,
			"subscribers": subs.subscribers,
			"icon": subs.icon_img
		}
	return (subreddits, 200)
	
if __name__ == "__main__":
    app.run()
