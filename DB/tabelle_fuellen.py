import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="AGM",
	passwd="1234",
	database="workautdb"
	)
	
mycursor = mydb.cursor()

#table_musclegrp
# mycursor.execute("INSERT INTO table_musclegrp(muscleGrp, name) VALUES(1, 'Brust')")
# mycursor.execute("INSERT INTO table_musclegrp(muscleGrp, name) VALUES(2, 'Ruecken')")
# mycursor.execute("INSERT INTO table_musclegrp(muscleGrp, name) VALUES(3, 'Beine')")
# mycursor.execute("INSERT INTO table_musclegrp(muscleGrp, name) VALUES(4, 'Schulter')")
# mycursor.execute("INSERT INTO table_musclegrp(muscleGrp, name) VALUES(5, 'Bauch')")
# mycursor.execute("INSERT INTO table_musclegrp(muscleGrp, name) VALUES(6, 'Arme')")



#table_subgrp
mycursor.execute("INSERT INTO table_subgrp VALUES(1, 1, 'ganze Brust')")
mycursor.execute("INSERT INTO table_subgrp VALUES(2, 1, 'obere Brust')")
mycursor.execute("INSERT INTO table_subgrp VALUES(3, 1, 'untere Brust')")
mycursor.execute("INSERT INTO table_subgrp VALUES(4, 2, 'Ruecken breite')")
mycursor.execute("INSERT INTO table_subgrp VALUES(5, 2, 'Ruecken tiefe')")
mycursor.execute("INSERT INTO table_subgrp VALUES(6, 2, 'unterer Ruecken')")
mycursor.execute("INSERT INTO table_subgrp VALUES(7, 3, 'komplett')")
mycursor.execute("INSERT INTO table_subgrp VALUES(8, 3, 'Beinstrecker')")
mycursor.execute("INSERT INTO table_subgrp VALUES(9, 3, 'Beinbeuger')")
mycursor.execute("INSERT INTO table_subgrp VALUES(10, 3, 'Aduktoren')")
mycursor.execute("INSERT INTO table_subgrp VALUES(11, 3, 'Abduktoren')")
mycursor.execute("INSERT INTO table_subgrp VALUES(12, 3, 'Po')")
mycursor.execute("INSERT INTO table_subgrp VALUES(13, 3, 'Waden')")
mycursor.execute("INSERT INTO table_subgrp VALUES(14, 4, 'vordere Schulter')")
mycursor.execute("INSERT INTO table_subgrp VALUES(15, 4, 'seitliche Schulter')")
mycursor.execute("INSERT INTO table_subgrp VALUES(16, 4, 'hintere Schulter')")
mycursor.execute("INSERT INTO table_subgrp VALUES(17, 5, 'Bauch')")
mycursor.execute("INSERT INTO table_subgrp VALUES(18, 5, 'seitliche Bauchmuskulatur')")
mycursor.execute("INSERT INTO table_subgrp VALUES(19, 6, 'Bizeps')")
mycursor.execute("INSERT INTO table_subgrp VALUES(20, 6, 'Trizeps')")

#Brust - 1 - ganze Brust: 1; obere Brust: 2; untere Brust: 3
mycursor.execute("INSERT INTO table_exercise VALUES(1, 'Bankdruecken', 1, 1)")
mycursor.execute("INSERT INTO table_exercise VALUES(2, 'Bankdruecken positiv', 1, 2)")
mycursor.execute("INSERT INTO table_exercise VALUES(3, 'Bankdruecken negativ', 1, 3)")
mycursor.execute("INSERT INTO table_exercise VALUES(4, 'Butterfly', 1, 1)")
mycursor.execute("INSERT INTO table_exercise VALUES(5, 'Brustpresse', 1, 1)")
mycursor.execute("INSERT INTO table_exercise VALUES(6, 'Liegestuetz', 1, 1)")
mycursor.execute("INSERT INTO table_exercise VALUES(7, 'Liegestuetz positiv', 1, 2)")
mycursor.execute("INSERT INTO table_exercise VALUES(8, 'Liegestuetz negativ', 1, 3)")
mycursor.execute("INSERT INTO table_exercise VALUES(9, 'Kabelzug unten', 1, 3)")
mycursor.execute("INSERT INTO table_exercise VALUES(10, 'Kabelzug oben', 1, 2)")
#Ruecken - 2 - Oberer Lat: 4; Unterer Lat: 5; unterer Ruecken: 6
mycursor.execute("INSERT INTO table_exercise VALUES(11, 'Klimmzuege breit', 2, 4)")
mycursor.execute("INSERT INTO table_exercise VALUES(12, 'Klimmzuege eng', 2, 4)")
mycursor.execute("INSERT INTO table_exercise VALUES(13, 'Latzug', 2, 4)")
mycursor.execute("INSERT INTO table_exercise VALUES(14, 'Rudern Langhantel', 2, 5)")
mycursor.execute("INSERT INTO table_exercise VALUES(15, 'Rudern Kurzhantel', 2, 5)")
mycursor.execute("INSERT INTO table_exercise VALUES(16, 'Rudern Maschine', 2, 5)")
mycursor.execute("INSERT INTO table_exercise VALUES(17, 'Rumänisches Kreuzheben', 2, 6)")
mycursor.execute("INSERT INTO table_exercise VALUES(18, 'Rudern Kabel', 2, 5)")
mycursor.execute("INSERT INTO table_exercise VALUES(19, 'Latzug eng', 2, 4)")
mycursor.execute("INSERT INTO table_exercise VALUES(20, 'Rückenstrecker', 2, 6)")
mycursor.execute("INSERT INTO table_exercise VALUES(21, 'Ueberzuege', 2, 4)")
#Beine - 3 - komplett: 7; Beinstrecker: 8; Beinbeuger: 9; Aduktoren: 10; Abduktoren: 11; Po: 12; Waden: 13
mycursor.execute("INSERT INTO table_exercise VALUES(22, 'Kniebeugen', 3, 7)")
mycursor.execute("INSERT INTO table_exercise VALUES(23, 'Beinstrecker', 3, 8)")
mycursor.execute("INSERT INTO table_exercise VALUES(24, 'Beinbeuger', 3, 9)")
mycursor.execute("INSERT INTO table_exercise VALUES(25, 'Beinpresse', 3, 7)")
mycursor.execute("INSERT INTO table_exercise VALUES(26, 'Sumo Kreuzheben', 3, 7)")
mycursor.execute("INSERT INTO table_exercise VALUES(27, 'Aduktoren Maschine', 3, 10)")
mycursor.execute("INSERT INTO table_exercise VALUES(28, 'Abduktoren', 3, 11)")
mycursor.execute("INSERT INTO table_exercise VALUES(29, 'Beinheber', 3, 12)")
mycursor.execute("INSERT INTO table_exercise VALUES(30, 'Abduktoren Kabel', 3, 10)")
mycursor.execute("INSERT INTO table_exercise VALUES(31, 'Wadenheben stehend', 3, 13)")
mycursor.execute("INSERT INTO table_exercise VALUES(32, 'Wadenheben sitzend', 3, 13)")
#Schulter - 4 - vordere Schulter: 14; seitliche Schulter: 15; hintere Schulter: 16
mycursor.execute("INSERT INTO table_exercise VALUES(33, 'Schulterdruecken Langhantel', 4, 14)")
mycursor.execute("INSERT INTO table_exercise VALUES(34, 'Schulterdruecken Kurzhnatel', 4, 14)")
mycursor.execute("INSERT INTO table_exercise VALUES(35, 'Seitheben Kurzhantel', 4, 15)")
mycursor.execute("INSERT INTO table_exercise VALUES(36, 'Seitheben Kabelzug', 4, 15)")
mycursor.execute("INSERT INTO table_exercise VALUES(37, 'Butterfly reverse', 4, 16)")
mycursor.execute("INSERT INTO table_exercise VALUES(38, 'Facepulls', 4, 16)")
mycursor.execute("INSERT INTO table_exercise VALUES(39, 'Frontheben', 4, 14)")
#Bauch - 5 - Bauch: 17; seitliche Bauchmuskulatur: 18
mycursor.execute("INSERT INTO table_exercise VALUES(40, 'Sit Ups', 5, 17)")
mycursor.execute("INSERT INTO table_exercise VALUES(41, 'Crunches seitlich', 5, 18)")
mycursor.execute("INSERT INTO table_exercise VALUES(42, 'Leg raises', 5, 17)")
mycursor.execute("INSERT INTO table_exercise VALUES(43, 'Klappmesser', 5, 17)")
mycursor.execute("INSERT INTO table_exercise VALUES(44, 'Toes to Bar', 5, 17)")
mycursor.execute("INSERT INTO table_exercise VALUES(45, 'Toes to Knee', 5, 17)")
mycursor.execute("INSERT INTO table_exercise VALUES(46, 'Unterarmstuetz', 5, 17)")
mycursor.execute("INSERT INTO table_exercise VALUES(47, 'Rumpfbeugen seitlich', 5, 18)")
mycursor.execute("INSERT INTO table_exercise VALUES(48, 'Rumpfbeugen seitlich Kurzhantel', 5, 18)")
#Arme - 6 - Bizeps: 19; Trizeps: 20
mycursor.execute("INSERT INTO table_exercise VALUES(49, 'Curls Kurzhantel', 6, 19)")
mycursor.execute("INSERT INTO table_exercise VALUES(50, 'Curls SZ-Stange', 6, 19)")
mycursor.execute("INSERT INTO table_exercise VALUES(51, 'Curls Kabel', 6, 19)")
mycursor.execute("INSERT INTO table_exercise VALUES(52, 'Hammer Curls', 6, 19)")
mycursor.execute("INSERT INTO table_exercise VALUES(53, 'Push Downs', 6, 20)")
mycursor.execute("INSERT INTO table_exercise VALUES(54, 'Push Downs einarmig', 6, 20)")
mycursor.execute("INSERT INTO table_exercise VALUES(55, 'French Press', 6, 20)")
mycursor.execute("INSERT INTO table_exercise VALUES(56, 'Kick Backs', 6, 20)")
mycursor.execute("INSERT INTO table_exercise VALUES(57, 'Dips', 6, 20)")
mycursor.execute("INSERT INTO table_exercise VALUES(58, 'Trizeps Dips', 6, 20)")

mydb.commit()
