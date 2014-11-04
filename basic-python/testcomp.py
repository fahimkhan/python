#!/usr/bin/python
import fileinput
print "Starting Point"
scancomplist=open("comp_list.txt",'r')
newcompval=open("comp_val.txt",'w+')
bakcompval=open("comp_valbak.txt",'r')
clist1=[]
cval=[]
clist2=[]
for compval in bakcompval:
	 cval.append(compval.strip())
	 clist2.append(compval.strip().partition(':')[0])
for complist in scancomplist:
	clist1.append(complist.strip())
print "Component Value List :",cval 
print "Component List1:",clist1
print "Component List2:",clist2
print "writing from comp_valbak.txt file to new comp_val.txt"
for reclist in open("comp_valbak.txt",'r'):
	line=reclist.split(':')
	print line[0]
	if line[0] in clist1:
		print "In clist1"
		newcompval.write(reclist)
	else:
		continue
print "writing from comp_list.txt to new comp_val.txt"
for recval in open("comp_list.txt",'r'):
	line=recval.strip()
	if line in clist2:
		print line,"Present in old list"
		continue
	else:
		print line,"Not present in old list"
		newcompval.write(line+":0")
		#newcompval.write(':0')
		newcompval.write('\n') 	
	
scancomplist.close()
newcompval.close()
bakcompval.close()		
print "End Script"
