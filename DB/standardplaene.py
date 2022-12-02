import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="AGM",
	passwd="1234",
	database="workautdb"
	)
	
mycursor = mydb.cursor()

# mycursor.execute("INSERT INTO table_user(uID, username, gender, pwd) VALUES(0, 'admin', 1, 'admin')")

# #Plaene
# mycursor.execute("INSERT INTO table_plan VALUES(1, 'Ganzkoerper Mann', 0)")
# mycursor.execute("INSERT INTO table_plan VALUES(2, 'GanzKoerper Frau', 0)")
# mycursor.execute("INSERT INTO table_plan VALUES(3, 'GanzKoerper Mann Cardio', 0)")
# mycursor.execute("INSERT INTO table_plan VALUES(4, 'GanzKoerper Frau Cardio', 0)")
# mycursor.execute("INSERT INTO table_plan VALUES(5, 'GanzKoerper Oberkoerper', 0)")
# mycursor.execute("INSERT INTO table_plan VALUES(6, 'GanzKoerper Unterkoerper', 0)")
# mycursor.execute("INSERT INTO table_plan VALUES(7, 'Bauch Beine Po', 0)")

#Plaene mit Uebungen fuellen
#GKM
sql = "INSERT INTO table_planex VALUES (%s, %s, %s, %s, %s)"
val = [
	(1, 60, 1, 1, 1), #1 WarmUp
	(1, 1, 2, 10, 3), #2 Bankdruecken
	(1, 4, 3, 15, 3), #3 Butterfly
	(1, 5, 4, 15, 3), #4 Brustpresse
	(1, 64, 5, 15, 3), #5 Schulterdruecken Maschine
	(1, 13, 6, 15, 3), #6 Latzug
	(1, 18, 7, 15, 3), #7 Rudern Kabel
	(1, 22, 8, 10, 3), #8 Kniebeugen
	(1, 23, 9, 15, 3), #9 Beinstrecker
	(1, 24, 10, 15, 3), #10 Beinbeuger
	(1, 20, 11, 15, 3), #11 Rueckenstrecker
	(1, 40, 12, 30, 3), #12 SitUps
	(1, 63, 13, 1, 1) #13 Cardio 20Min
]

mycursor.executemany(sql, val)

#GKF
sql = "INSERT INTO table_planex VALUES (%s, %s, %s, %s, %s)"
val = [
	(2, 60, 1, 1, 1), #1 WarmUp
	(2, 22, 2, 10, 3), #2 Kniebeugen
	(2, 59, 3, 15, 3), #3 Ausfallschritte
	(2, 23, 4, 15, 3), #4 Beinstrecker
	(2, 24, 5, 15, 3), #5 Beinbeuger
	(2, 25, 6, 15, 3), #6 Beinpresse
	(2, 13, 7, 15, 3), #7 Latzug
	(2, 16, 8, 15, 3), #8 Rudern Maschine
	(2, 5, 9, 15, 3), #9 Brustpresse
	(2, 20, 10, 15, 3), #10 Rückenstrecker
	(2, 47, 11, 15, 3), #11 Rumpfbeugen seitlich
	(2, 40, 12, 30, 3), #12 SitUps
	(2, 63, 13, 1, 1) #13 Cardio 20Min
]

mycursor.executemany(sql, val)

#GKMC
sql = "INSERT INTO table_planex VALUES (%s, %s, %s, %s, %s)"
val = [
	(3, 60, 1, 1, 1), #1 WarmUp
	(3, 1, 2, 15, 3), #2 Bankdruecken
	(3, 4, 3, 20, 3), #3 Butterfly
	(3, 64, 4, 20, 3), #4 Schulterdruecken Maschine
	(3, 13, 5, 20, 3), #5 Latzug
	(3, 18, 6, 20, 3), #6 Rudern Kabel
	(3, 22, 7, 15, 3), #7 Kniebeugen
	(3, 23, 8, 20, 3), #8 Beinstrecker
	(3, 24, 9, 20, 3), #9 Beinbeuger
	(3, 20, 10, 20, 3), #10 Rueckenstrecker
	(3, 40, 11, 30, 3), #11 SitUps
	(3, 61, 12, 1, 1) #12 Cardio 30Min
]

mycursor.executemany(sql, val)

#GKFC
sql = "INSERT INTO table_planex VALUES (%s, %s, %s, %s, %s)"
val = [
	(4, 60, 1, 1, 1), #1 WarmUp
	(4, 22, 2, 15, 3), #2 Kniebeugen
	(4, 59, 3, 20, 3), #3 Ausfallschritte
	(4, 23, 4, 20, 3), #4 Beinstrecker
	(4, 24, 5, 20, 3), #5 Beinbeuger
	(4, 13, 6, 20, 3), #6 Latzug
	(4, 16, 7, 20, 3), #7 Rudern Maschine
	(4, 5, 8, 20, 3), #8 Brustpresse
	(4, 20, 9, 20, 3), #9 Rückenstrecker
	(4, 47, 10, 20, 3), #10 Rumpfbeugen seitlich
	(4, 40, 11, 30, 3), #11 SitUps
	(4, 61, 12, 1, 1) #12 Cardio 30Min
]

mycursor.executemany(sql, val)

#Oberkoerper
sql = "INSERT INTO table_planex VALUES (%s, %s, %s, %s, %s)"
val = [
	(5, 60, 1, 1, 1), #1 WarmUp
	(5, 1, 2, 10, 3), #2 Bankdruecken
	(5, 4, 3, 15, 3), #3 Butterfly
	(5, 57, 4, 15, 3), #4 Dips
	(5, 34, 5, 15, 3), #5 Schulterdruecken Kurzhantel
	(5, 35, 6, 15, 3), #6 Seitheben Kurzhantel
	(5, 13, 7, 15, 3), #7 Latzug
	(5, 14, 8, 15, 3), #8 Rudern Langhantel
	(5, 21, 9, 15, 3), #9 Ueberzuege
	(5, 37, 10, 15, 3), #10 Butterfly Reverse
	(5, 50, 11, 15, 3), #11 Curls SZ-Stange
	(5, 53, 12, 15, 3), #12 Push Downs
	(5, 63, 13, 1, 1) #13 Cardio 20Min
]

mycursor.executemany(sql, val)

#Unterkoerper
sql = "INSERT INTO table_planex VALUES (%s, %s, %s, %s, %s)"
val = [
	(6, 60, 1, 1, 1), #1 WarmUp
	(6, 22, 2, 10, 3), #2 Kniebeugen
	(6, 23, 3, 15, 3), #3 Beinstrecker
	(6, 24, 4, 15, 3), #4 Beinbeuger
	(6, 59, 5, 15, 3), #5 Ausfallschritte
	(6, 25, 6, 15, 3), #6 Beinpresse
	(6, 27, 7, 15, 3), #7 Aduktoren Maschine
	(6, 28, 8, 15, 3), #8 Abduktoren Maschine
	(6, 20, 9, 15, 3), #9 Rueckenstrecker
	(6, 47, 10, 15, 3), #10 Rumpfbeugen seitlich
	(6, 40, 11, 30, 3), #11 SitUps
	(6, 41, 12, 30, 3), #12 Crunches seitlich
	(6, 63, 13, 1, 1) #13 Cardio 20Min
]

mycursor.executemany(sql, val)

#Bauch, Beine, Po
sql = "INSERT INTO table_planex VALUES (%s, %s, %s, %s, %s)"
val = [
	(7, 60, 1, 1, 1), #1 WarmUp
	(7, 22, 2, 15, 3), #2 Kniebeugen
	(7, 23, 3, 20, 3), #3 Beinstrecker
	(7, 24, 4, 20, 3), #4 Beinbeuger
	(7, 59, 5, 20, 3), #5 Ausfallschritte
	(7, 27, 6, 20, 3), #6 Aduktoren Maschine
	(7, 28, 7, 20, 3), #7 Abduktoren Maschine
	(7, 29, 8, 20, 3), #8 Beinheber
	(7, 20, 9, 20, 3), #9 Rueckenstrecker
	(7, 47, 10, 20, 3), #10 Rumpfbeuger seitlich
	(7, 40, 11, 30, 3), #11 SitUps
	(7, 41, 12, 30, 3), #12 Crunches seitlich
	(7, 62, 13, 1, 1) #13 Cardio 25Min
]
	
mycursor.executemany(sql, val)


mydb.commit()