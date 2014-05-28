#!/bin/bash 

#FILES=$1/*
FILES=$1
EXT_LOC=$2

##Extracting each lecture file to standard format
for i in {1..20}
  do
    echo "File name is : forum-$i.xml" 
    python parse_moodle_new.py $FILES/forum-$i.xml $EXT_LOC 
    rm $1/*.txt 
  done

##Adding all file name in array sequentially
for i in {1..20}
  do
    array[i]=$EXT_LOC/$i.xml
  done 

##Merging all the extarcted lecture file into one

python combine-xml.py "${array[@]}" | sponge final.xml



