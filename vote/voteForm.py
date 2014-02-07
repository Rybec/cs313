import sys
sys.path.append('/home/pi/public_html/libs')
from web import *

def index(req):
	# Center content area
	formElements = h(3, "What is your favorite steampunk prop?")  + \
	               radio("prop", "Goggles", 'checked="checked"') + \
                        	label("Goggles") + br() + \
	               radio("prop", "Top hat") + \
			 	label("Top hat") + br() + \
	               radio("prop", "Corset") + \
			 	label("Corset") + br() + \
	               radio("prop", "Gun") + \
			 	label("Gun") + br() + \
	               submit()

	formdata = form(formElements,
	                name   = "input",
                        action = "index.py",
                        method = "POST")

	resultsPage = br() + anchor("Go straight to results", "index.py?results")


	html = div(formdata + resultsPage)

	return html
