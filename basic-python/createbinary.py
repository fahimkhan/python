#!/usr/bin/python

str='Hello World!'
f=open("filebinary.bin","wb")
f.write(str.encode('utf-8'))
f.close()
f=open("filebinary.bin","rb")
fcontent=f.read()
f.close()
print "The content in the file is :"

print fcontent.decode('utf-8')

