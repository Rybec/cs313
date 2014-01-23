from mod_python import Cookie
from web import *
import voteForm
import results

def index(req):
	html = html5open() + head("Ben Williams' Votes Page", css = "../main.css")
	html = html + bodyOpen()

	# Header/title
	html = html + div(img("../BLLogo3d_small.png"), attrib='class="logo"')
	html = html + div("<h1>Ben Williams' Home Page</h1>", attrib='class="title"')

	# Left side navigation menu
	menu = anchor("Assignments", "../index.py")

	html = html + div("<h4>Menu</h4>" + menu, attrib='class="leftSidebar"')

	# Center content area
	content = ""

	if ("vote" in Cookie.get_cookies(req).keys() or
	    "results" in req.form.keys() or
	    "prop" in req.form.keys()):
		content = results.index(req)
	else:
		content = voteForm.index(req)


	html = html + div(content, attrib = 'class="centerArea"')

	# Right side asides and other notes
	sidenotes = "On the Assignments page, the links are not obvious, " + \
                    " because coloring them would ruin the aesthetic."

	html = html + div("<h4>Asides</h4>" + p(sidenotes), attrib='class="rightSidebar"')

	# Footer
	html = html + div("Important information here, like copyright.", attrib='class="footer"')


	html = html + bodyClose()
	html = html + html5close()

	return html
