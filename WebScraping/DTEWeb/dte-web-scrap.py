#!/usr/bin/env python

from bs4 import BeautifulSoup
import re
import json
import ast
import requests
import csv


instiUrl = "http://www.dtemaharashtra.gov.in/approvedinstitues/StaticPages/frmInstituteSummary.aspx?InstituteCode=" 
instiCodeList = []
bad_list = []
extracted_list = {}


f = csv.writer(open("List_Of_Institute.csv", "w"))
f.writerow(["Institute Name", "DTE Region","Region Type","Address","District","Taluka","Pincode","Std Code","Website","Email","Head Name","Office Number","Personal Number"]) 

##Getting code of all institute 

soup = BeautifulSoup(open("CodeInstitute.html"))
tablecontent = soup.find(id="ctl00_rightContainer_ContentTable1_gvInstituteList")

for code in tablecontent.find_all("a"):
	#print instiUrl+code.text	
	instiCodeList.append(code.text)
	
##Scraping for all code
for code in instiCodeList:
    newurl = instiUrl+code
    if (newurl != None):
    	print "New Url ",newurl
    	collegeInfoContent = requests.get(newurl)
    	newsoup = BeautifulSoup(collegeInfoContent.content)
    	v_insti_name = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblInstituteNameEnglish")
    	v_dte_region = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblRegion")
    	v_region_type = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblRegionType")
    	v_address = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblAddressEnglish")
    	v_district = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblDistrict")
    	v_taluka = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblTaluka")
    	v_pincode = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblPincode")
    	v_stdcode = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblSTDCode")
    	v_website = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblWebAddress")
    	v_email = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblEMailAddress")
    	v_director_principle_name = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblPrincipalNameEnglish")
    	v_office_number = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblOfficePhoneNo")
    	v_personal_number = newsoup.find(id="ctl00_rightContainer_ContentBox1_lblPersonalPhoneNo")
    else:
    	bad_list.append(code)

    try:
    	f.writerow([v_insti_name.text,v_dte_region.text,v_region_type.text,v_address.text,v_district.text,v_taluka.text,v_pincode.text,v_stdcode.text,v_website.text,v_email.text,v_director_principle_name.text,v_office_number.text,v_personal_number.text])
    except (UnicodeEncodeError,AttributeError):
		bad_list.append(code)

    	
print "Bad List ",bad_list
