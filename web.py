from cgi import escape
from urllib import unquote

def html5open():
	return "<!DOCTYPE html>\n<html>\n"

def html5close():
	return "</html>"

def head(title, css = ""):
	html = "<head>"
	html = html + '<meta http-equiv="Content-type" content="text/html;charset=UTF-8"/>'

	if (css != ""):
		html = html + '<link rel="stylesheet" type="text/css" href="' + css + '"/>'

	html = html + "<title>" + title + "</title>"
	html = html + "</head>\n"
	return html

def bodyOpen():
	return '<body>\n'

def bodyClose():
	return "</body>\n"

def anchor(text, url):
	return "<a href=\"" + url + "\">" + text + "</a>\n"

def div(inner, attrib = ""):
	return "<div " + attrib + ">" + inner + "</div>"

def p(text, attrib = ""):
	return "<p " + attrib + ">" + text + "</p>"

def pre(text, attrib = ""):
	return "<pre " + attrib + ">" + text + "</pre>"

def img(src, attrib = ""):
	return '<img src="' + src + '" ' + attrib + "/>"