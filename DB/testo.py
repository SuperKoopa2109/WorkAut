import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="AGM",
	passwd="1234",
	database="workaut"
	)
	
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM uebung");

myresult = mycursor.fetchall()

for x in myresult:
	print(x)