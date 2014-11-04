#!/usr/bin/python
import re
str1 = "this is string example....wow!!!";
str2 = "exam";
str3="Hello"
print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

if str1.find(str3,10):
    print "Found"
else:
    print "Not found"

str4="Hello World"
str5="world"

if str5 in str4:
    print "Find",str5
else:
    print "Not Found"    

if re.search(str5,str4,re.IGNORECASE):
    print "Pattern Find"
else:
    print "Pattern not found"    
