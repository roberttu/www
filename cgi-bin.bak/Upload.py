#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

#cgitb.enable()
cgitb.enable(display=0,logdir="/var/www/html/cgi-bin")
form = cgi.FieldStorage()
#print """\
#Content-Type: text/html\n
#<html><body>"""
#print "<p>"
#print form['fileToUpload'].filename
#print "</p>"
#print """\
#</body></html>
#""" % (message,)
#exit(0)

# A nested FieldStorage instance holds the file
fileitem = form['fileToUpload']

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('/var/www/html/Uploads/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)
