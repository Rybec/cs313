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

def form(controls, name = "", action = "", method = "", attrib = ""):
	return '<form ' + \
	       attrib + " " + \
	       ('name="'   + name   + '" ' if (name   != "") else "") + \
	       ('action="' + action + '" ' if (action != "") else "") + \
	       ('method="' + method + '" ' if (method != "") else "") + \
	       '>' + controls + '</form>'

def textbox(name = "", value = "", attrib = ""):
	return input("text", name = name, value = value, attrib = attrib)

def radio(name = "", value = "", attrib = ""):
	return input("radio", name = name, value = value, attrib = attrib)

def check(name = "", value = "", attrib = ""):
	return input("checkbox", name = name, value = value, attrib = attrib)

def textarea(name = "", value = "", rows = "", cols = ""):
	return '<textarea ' + \
	       ('name="'  + name  + '" ' if (name  != "") else "") + \
	       ('value="' + value + '" ' if (value != "") else "") + \
	       ('rows="'  + rows  + '" ' if (rows  != "") else "") + \
	       ('cols="'  + cols  + '" ' if (cols  != "") else "") + \
	       '></textarea>'
	       

def submit(name = "", attrib = ""; value = "Submit"):
	return input("submit", value)


def input(type, name = "", value = "", attrib = ""):
	return '<input ' + \
	       attrib + ' ' + \
	       'type="'  + type  + '" ' + \
	       ('name="'  + name  + '" ' if (name  != "") else "") + \
	       ('value="' + value + '" ' if (value != "") else "") + \
	       '/>'
def label(text):
	return '<label>' + text + '</label>'

def br():
	return '<br/>'

def h(num, text):
	return '<h' + str(num) + '>' + text + '</h' + str(num) + '>'
