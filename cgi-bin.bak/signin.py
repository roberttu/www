#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules
import cgi, string, sys, md5crypt
import cgitb

# Required header that tells the browser how to render the HTML.
cgitb.enable()
#print "Content-Type: text/html\n\n"
print "Content-Type: text/plain\n\n"

# Define function to generate HTML form.
def generate_form():
	print "<HTML>\n"
	print "<HEAD>\n"
	print "\t<TITLE>Info Form</TITLE>\n"
	print "</HEAD>\n"
	print "<BODY BGCOLOR = white>\n"
	print "\t<H3>Please, enter your username and password.</H3>\n"
	print "\t<TABLE BORDER = 0>\n"
	print "\t\t<FORM METHOD = post ACTION = \
	\"signin.py\">\n"
	print "\t\t<TR><TH>Username:</TH><TD><INPUT TYPE = text \
	NAME = \"username\"></TD><TR>\n"
	print "\t\t<TR><TH>Password:</TH><TD><INPUT \
	TYPE = password NAME = \"password\"></TD></TR>\n"
	print "\t</TABLE>\n"
	print "\t<INPUT TYPE = hidden NAME = \"action\" VALUE = \
	\"display\">\n"
	print "\t<INPUT TYPE = submit VALUE = \"Enter\">\n"
	print "\t</FORM>\n"
	print "</BODY>\n"
	print "</HTML>\n"

	# Define function to test the password.
def test(id, passwd):
	passwd_file = open('passwords.txt', 'r')
        for line in passwd_file:
#	line = passwd_file.readline()
		combo = string.split(line, ":")
                if (id == combo[0]):
			encrypted_pw = md5crypt.unix_md5_crypt(passwd, 'ab')
		        if (encrypted_pw[0:20] == combo[1][0:20]):
			   return "passed"
		        else:
		 	   return "failed"
        return "failed"
	passwd_file.close()

	# Define function display_page.
def display_redirect():
  redirectURL="/main.html"
  print 'Location: %s' % redirectURL
  print # HTTP says you have to have a blank line between headers and content
  print '<html>'
  print '  <head>'
  print '    <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
  print '    <title>You are going to be redirected</title>'
  print '  </head>' 
  print '  <body>'
  print '    Redirecting... <a href="%s">Click here if you are not redirected</a>' % redirectURL
  print '  </body>'
  print '</html>'
def display_page(result):
	print "<HTML>\n"
	print "<HEAD>\n"
	print "\t<TITLE>Info Form</TITLE>\n"
	print "</HEAD>\n"
	print "<BODY BGCOLOR = white>\n"
	if (result == "passed"):
		 print "You entered the correct combo.\n"
	else:
		 print "You entered the incorrect combo.\n"
	print "</BODY>\n"
	print "</HTML>\n"

	# Define main function.
def main():
	form = cgi.FieldStorage()
       
	if (form.has_key("inputEmail") \
	and form.has_key("inputPassword")):
#		 if (form["action"].value == "display"):
		    result = test(form["inputEmail"].value, form["inputPassword"].value)
                    if result=="passed":                   
		      display_redirect()
                    else:
#                      form["errormessage"].innerHTML="User/password combo incorrect."
                       print "Incorrect password. Try again"
#		      display_page(result)
#		    display_page(result)
#	else:
#		 generate_form()

# Call main function.
main()
