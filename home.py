import sys
sys.path.append("/home/pi/public_html/libs")
from web import *

def index(req):
	html = html5open() + head("Ben Williams' Home Page", css = "main.css")
	html = html + bodyOpen()

	# Header/title
	html = html + div(img("BLLogo3d_small.png"), attrib='class="logo"')
	html = html + div("<h1>Ben Williams' Home Page</h1>", attrib='class="title"')

	# Left side navigation menu
	menu = anchor("Assignments", "index.py")

	html = html + div("<h4>Menu</h4>" + menu, attrib='class="leftSidebar"')

	# Center content area
	centerText = "My name is Ben Williams.  I am a CS major at BYU-Idaho, " + \
	             "and I am a senior.  I am taking CS313.  I already have " + \
	             "some experience in web design, so I am using this as an " + \
                     "opportunity to learn CGI scripting using Python."

	html = html + div(p(centerText), attrib = 'class="centerArea"')

	# Right side asides and other notes
	sidenotes = "On the Assignments page, the links are not obvious, " + \
                    " because coloring them would ruin the aesthetic."

	html = html + div("<h4>Asides</h4>" + p(sidenotes), attrib='class="rightSidebar"')

	# Footer
	html = html + div("Important information here, like copyright.", attrib='class="footer"')


	html = html + bodyClose()
	html = html + html5close()

	return html
