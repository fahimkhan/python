#!/usr/bin/python 

#from xml.etree import ElementTree as ET
from lxml import etree as ET
from bs4 import BeautifulSoup
import sys
import os
import re

def removehtmltag(htmltxt):
    if htmltxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmltxt).findAll(text=True)) 



input_file=sys.argv[1]
ext_loc=sys.argv[2]

if ext_loc.endswith('/'):
  print "Proper"
  pass
else:
  print "Not Proper"
  ext_loc=ext_loc+'/'
  print "After proper",ext_loc

outfile=input_file.split('/')[-1]

print "Input File",input_file,os.path.splitext(input_file)[1]

##Checking for xml file
if os.path.splitext(input_file)[1]=='.xml':
    pass
else:
    print "Please provide proper xml file"    
    sys.exit()

tree=ET.parse(input_file)
root=tree.getroot()

print "Root Tag ",root

zero=root.getchildren()[0]
print "Zero",zero

#list_of_forum_id=[]
#list_of_forum_id_name=[]

fob=open(input_file+".txt",'w')

main_root=ET.Element("DISCUSSIONS")




for child in root.findall('forum'):
  #print "Child in forum is ",child.getchildren()
  add_discussion=ET.SubElement(main_root,"DISCUSSION")
  add_id=ET.SubElement(add_discussion,"ID")
  add_id.text=child.get('id')
  add_lecture=ET.SubElement(add_discussion,"LECTURE")         
  add_posts=ET.SubElement(add_discussion,"POSTS") 
  #add_lecture.text=os.path.splitext(input_file)[0]                      
  add_lecture.text=outfile                      
  for subchild in child.findall('discussions'):
    #print "subchild in discussion is " ,subchild.getchildren()
    for item1 in subchild.findall('discussion'):
      #print "Item under discussion are ",item1.getchildren()
      #print "Attrbute of discussion is ",item1.attrib
      for item2 in item1.findall('posts'):
        #print "Posts : ",item2.getchildren()
        add_post=ET.SubElement(add_posts,"POST")
        for item3 in item2.findall('post'):
          #print "Child of POST",item3.getchildren()
          #print "Subject:",item3.findtext('subject')
          #print "Message:",item3.findtext('message')
          #fob.write(str(item3.findtext('SUBJECT')))
          add_subject=ET.SubElement(add_post,"SUBJECT")
          add_subject.text=item3.findtext('subject')
          temp1=(item3.findtext('subject').encode('utf-8'))
          fob.write(temp1+'\n')
          #fob.write(str(item3.findtext('\n')))
          add_messg=ET.SubElement(add_post,'MESSAGE')
          add_messg.text=item3.findtext('message')
          temp2=(item3.findtext('message').encode('utf-8'))
          #fob.write(item3.findtext('MESSAGE'))
          fob.write(temp2+'\n')
  
fob.close()
#myxml=ET.ElementTree(main_root)
#myxml.write("extract_data_"+input_file, pretty_print=True)
foutname=outfile.split('-')[-1]
ET.ElementTree(main_root).write(ext_loc+foutname,pretty_print=True)

#Make it Beautiful
f1=open(input_file+".txt",'r')
content=f1.read()
out=removehtmltag(content).encode('utf-8')
f2=open("output.txt",'w')
f2.write(out)
f2.close()
f1.close()
  
