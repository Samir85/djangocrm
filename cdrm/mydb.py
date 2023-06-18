import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd = '0000',
)

# prepare a cursor object 
cursorObject =database.cursor()

# create database 
cursorObject.execute("CREATE DATABASE samir")

print ('all done ! ')