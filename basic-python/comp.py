#!/usr/bin/python
import fileinput
print "Starting Point"
scancomplist=open("comp_list.txt",'r')
appendcompval=open("comp_val.txt",'w')
bakcompval=open("comp_val.bak",'r')
clist=[]
cval=[]
for compval in appendcompval:
	 cval.append(compval.strip().partition(':')[0])
for complist in scancomplist:
	clist.append(complist.strip().partition(':')[0])
print "Component Value List :",cval 
print "Component List:",clist

for line in fileinput.input(['comp_list.txt']):
	print "Comp List Loop"
	print line.strip()
	if line.strip() in cval:
		continue
	else:
		appendcompval.write(line.strip()+':0')
		appendcompval.write('\n')
for line in fileinput.input(['comp_val.txt']):
	print "Comp val loop"
	print line.strip()
	if line.strip().partition(':')[0] in clist:
		print "Continue of second for loop"
		continue
	else:
		print "Else of second for loop"
		#print line.read()
		
	 

scancomplist.close()
appendcompval.close()

print "End Script"
