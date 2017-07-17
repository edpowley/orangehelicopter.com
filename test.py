#!/usr/local/bin/python2.7

import sys, platform

print "Content-Type: text/html;charset=utf-8"
print

print "<html><body>"
print "<h1>Hello World!</h1>"

print "<h2>sys.version</h2>"
print "<pre>%s</pre>" % sys.version

print "<h2>platform.architecture()</h2>"
print "<pre>%r</pre>" % platform.architecture
print "</body></html>"
