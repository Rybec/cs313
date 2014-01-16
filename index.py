from web import *
from assignments import *

def index(req):
	html = html5open() + head("Ben Williams' Assignments Page", css = "dos.css")
	html = html + bodyOpen()

#	html = html + div(p("Ben Williams' CS313 Assignments Page", attrib = 'class="title"'))
#	html = html + "<br/>"
#	html = html + anchor("Home page", "home.py")
	html = html + dir()

	html = html + bodyClose()
	html = html + html5close()

	return html

def dir():
	html = "<pre>\n"
	html = html + "C:\>dir\n\n"
	html = html + " Volume in drive C is assignments\n"
	html = html + " Volume Serial Number is 1FFF-F000\n"
	html = html + " Directory of C:\\\n\n"
	html = html + assignmentsHTML()
	html = html + "C:\>_"
	html = html + "</pre>\n"

	return html
