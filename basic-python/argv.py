#!/usr/bin/python
import subprocess
from sys import argv

scriptname,fname=argv

print "The script is called:",scriptname
print "The first arguement is :",fname

subprocess.call(["unzip" ,fname])
