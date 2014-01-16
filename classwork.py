from web import *
from assignments import *

def index(req):
	html = html5open() + head("Ben Williams' Random Class Work", css = "dos.css")
	html = html + bodyOpen()

	d = {"key1":"Item1", "key2":"Item2", "key3":"Item3"}
	keys = d.keys()
	keys.sort()

	for i in keys:
		html = html + div(d[i], attrib = 'id="' + i +'"')


	html = html + bodyClose()
	html = html + html5close()

	return html

