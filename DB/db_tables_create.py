import mysql.connector


#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
# def hello():
    # return "<input type='Submit' value='ASDF' width=0.5em length=0.5em action='www.google.de'>"
	
mydb = mysql.connector.connect(
	host="localhost",
	user="AGM",
	passwd="1234",
	database="workautdb"
	)
	
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE table_group(gID tinyint NOT NULL, gName Text NOT NULL, CONSTRAINT PK_group PRIMARY KEY(gID))")
#mycursor.execute("CREATE TABLE table_assign(aID tinyint NOT NULL, gID tinyint, gender bit, goal tinyint, tpw tinyint, CONSTRAINT PK_assign PRIMARY KEY(aID), CONSTRAINT FK_assign FOREIGN KEY(gID) REFERENCES table_group(gID))") 
mycursor.execute("CREATE TABLE table_planGroup(pgID tinyint NOT NULL, gID tinyint NOT NULL, pID int NOT NULL, CONSTRAINT PK_planGroup PRIMARY KEY(pgID), CONSTRAINT FK_planGroupG FOREIGN KEY(gID) REFERENCES table_group(gID), CONSTRAINT FK_planGroupP FOREIGN KEY(pID) REFERENCES table_plan(pID))")

#mycursor.execute("CREATE DATABASE workautdb")

#mycursor.execute("CREATE TABLE table_muscleGrp(muscleGrp int NOT NULL, name Text NOT NULL, CONSTRAINT PK_muscleGrp PRIMARY KEY (muscleGrp))")
#mycursor.execute("CREATE TABLE table_subGrp(subGrp int NOT NULL, name Text, CONSTRAINT PK_subGrp PRIMARY KEY (subGrp))")
#mycursor.execute("CREATE TABLE table_exercise(eID int NOT NULL, name Text NOT NULL, muscleGrp int NOT NULL, subGrp int, CONSTRAINT PK_exe PRIMARY KEY (eID), CONSTRAINT FK_muscleGrp FOREIGN KEY (muscleGrp) REFERENCES table_muscleGrp(muscleGrp), CONSTRAINT FK_subGrp FOREIGN KEY (subGrp) REFERENCES table_subgrp(subgrp))")
#mycursor.execute("CREATE TABLE table_user(uID int NOT NULL, username Text NOT NULL, gender bit NOT NULL, goal tinyint, tpw tinyint, pwd varchar(32), CONSTRAINT PK_uID PRIMARY KEY (uID))")
#mycursor.execute("CREATE TABLE table_plan(pID int NOT NULL, pName tinytext NOT NULL, uID int NOT NULL, CONSTRAINT PK_pID PRIMARY KEY (pID), CONSTRAINT FK_uID FOREIGN KEY (uID) REFERENCES table_user(uID))")
#mycursor.execute("CREATE TABLE table_planEx(pID int NOT NULL, eID int NOT NULL, position tinyint NOT NULL, CONSTRAINT PK_planEx PRIMARY KEY (pID, eID))")

#myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)