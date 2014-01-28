from mod_python import Cookie
from web import *
import time
import os

def index(req):

	# Apache does not run the script from the directory it is in.
	# This changes the working directory to the directory this file is in.
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	# Center content area
	myVote = ""
	if ("prop" in req.form.keys() and
	    "vote" not in Cookie.get_cookies(req).keys()):
		myVote = h(4, "You voted for " + req.form["prop"])
		with open("../data/votes.txt", "a") as file:
			file.write(req.form["prop"] + "\n")
		cookie = Cookie.Cookie('vote', req.form["prop"])
		cookie.expires = time.time() + 3600 # An hour
		Cookie.add_cookie(req, cookie)

	votes = ""
	with open("../data/votes.txt", "r") as file:
		votes = file.read()

	tally = {}
	for i in set(votes.strip().split("\n")):
		tally[i] = votes.split("\n").count(i)

	results = "<div><h3>Results</h3>"
	results += '<table class="side">'
	for i in tally.keys():
		results += "<tr><th>" + i + "</th>" + \
		           "<td>" + str(tally[i]) + "</td></tr>"

	results += "</table></div>"

	html = myVote + results

	return html
