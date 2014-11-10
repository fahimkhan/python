#!/usr/bin/python 

#This script create employee table under database mytestdb from user mytestuser

import MySQLdb

#Open db connection<server,username,password,database_name>
db = MySQLdb.connect("localhost","mytestuser","test123","mytestdb")

#Prepare cursor object 
cursor = db.cursor()

#Drop table if exist
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Create table
sql="""create table employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        gender char(1),
        income float
    )"""

cursor.execute(sql)

#Disconnect
db.close()
