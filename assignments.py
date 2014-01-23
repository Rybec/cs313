import os
import time

# Apache does not run the script from the directory it is in.
# This changes the working directory to the directory this file is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# List of assignments
assignments = [
#	(text (Max 20 characters), href)
	("HOME_PAGE", "home.py"),
	("PYTHON_SURVEY", "vote/index.py"),
]

# os.stat().st_ctime  Create time
# os.stat().st_atime  Last Access time
# os.stat().st_mtime  Last Modify time
# os.stat().st_size   File size
# os.stat() returns a struct including a bunch of other data as well

def assignmentsHTML():
	html = ""
	bytes = 0
	for i in assignments:
		fdata = os.stat(i[1])
		# Get last modified date, and format to DOS format
		mdate = time.strftime("%m-%d-%y", time.localtime(fdata.st_mtime))
		# Get last modified time, and format to DOS format
		mtime = time.strftime("%I", time.localtime(fdata.st_mtime)).strip("0") + \
		        time.strftime(":%M", time.localtime(fdata.st_mtime)) + \
		        time.strftime("%p", time.localtime(fdata.st_mtime)).lower()[0]
		# Get file size, and format to DOS format
		fsize = '{:,}'.format(fdata.st_size)
		elem = '{}{:>13}{:>9}{:>8}'.format(a('{:<21}'.format(i[0]), i[1]), fsize, mdate, mtime)
		html = html + elem + "\n"

		bytes = bytes + os.path.getsize(i[1])

	files = len(assignments)
	free = 8589869056 - bytes

        html = html + '{:>18} file(s){:>14,} bytes\n'.format(files, bytes)
        html = html + '{:>40} bytes free\n'.format('{:,}'.format(free))


	return html

# Anchor without following newline
def a(text, href):
	return '<a href="' + href + '">' + text + '</a>'
