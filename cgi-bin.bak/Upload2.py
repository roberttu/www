#!/usr/bin/python
import cgi, os,shutil
import json
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

#cgitb.enable()
cgitb.enable(display=0,logdir="/var/www/html/logs")
form = cgi.FieldStorage()
result=form['fileToUpload']
#print """\
#Content-Type: text/html\n
#<html><body>"""
#print "<p>"
#print result
#print "</p>"
#print """\
#</body></html>
#""" % (message,)
#exit(0)

# A nested FieldStorage instance holds the file
#fileitem = form['fileToUpload']

# Test if the file was uploaded
message=""
if 1:

    # strip leading path from file name
    # to avoid directory traversal attacks
    filefield=form['fileToUpload']
    if not isinstance(filefield, list):
        filefield=[filefield]
    for fileitem in filefield:
	    fn = os.path.basename(fileitem.filename)
         
	    with open('/var/www/html/Uploads/' + fn, 'wb') as f:
               shutil.copyfileobj(fileitem.file,f )
	    message = message+ 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)
