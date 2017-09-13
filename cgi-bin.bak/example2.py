#!/usr/local/bin/python

import cgi
import cgitb; cgitb.enable()
import os

try: # Windows needs stdio set for binary mode.
        import msvcrt
        msvcrt.setmode ( 0, os.O_BINARY ) # stdin  = 0
        msvcrt.setmode ( 1, os.O_BINARY ) # stdout = 1
except ImportError:
        pass

#This variable specifies relative path to the folder, where the gallery 
#with uploaded files is located.
galleryPath = "../Uploads/"

#Process upload.

print "Content-Type: text/html\r\n\r\n\r\n"

absGalleryPath = os.path.abspath( galleryPath )
absThumbnailsPath = os.path.join( absGalleryPath, "Thumbnails" )

form = cgi.FieldStorage()

#Get total number of uploaded files (all files are uploaded in a single package).
fileCount = int( form.getfirst( "FileCount", "0" ) );

#Iterate through uploaded data and save the original file and thumbnail.
for i in range( 1, fileCount + 1 ):
        #Get source file and save it to disk.
        sourceFile = form["SourceFile_" + str( i )];                    
        fileName = os.path.basename( sourceFile.filename )
        f = open ( os.path.join( absGalleryPath, fileName ), 'wb' )
        while 1:
                chunk = sourceFile.file.read( 10000 )
                if not chunk: 
                        break   
                f.write( chunk )
        f.close()
                
        #Get first thumbnail (the single thumbnail in this code sample) and save it to disk.
        thumbnail1File = form["Thumbnail1_" + str( i )];
        f = open ( os.path.join( absThumbnailsPath, fileName + ".jpg" ), 'wb' )
        while 1:
                chunk = thumbnail1File.file.read( 10000 )
                if not chunk: 
                        break   
                f.write( chunk )
        f.close()
