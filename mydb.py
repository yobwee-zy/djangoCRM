import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = '',
    passwd = ''
)

#prep cursor object
cursorObject = dataBase.cursor()

#Create db
cursorObject.execute("CREATE DATABASE mydb")
print('Db created success!')
