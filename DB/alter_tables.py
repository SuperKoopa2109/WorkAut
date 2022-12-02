import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="AGM",
	passwd="1234",
	database="workautdb"
	)
	
mycursor = mydb.cursor()

# mycursor.execute("INSERT INTO table_musclegrp VALUES(100, 'WarmUp')")
# mycursor.execute("INSERT INTO table_subgrp VALUES(100, 100, 'WarmUp')")
# mycursor.execute("INSERT INTO table_musclegrp VALUES(101, 'Cardio')")
# mycursor.execute("INSERT INTO table_subgrp VALUES(101, 101, 'Cardio')")

#mycursor.execute("INSERT INTO table_exercise VALUES(59, 'Ausfallschritte', 3, 7)")
#mycursor.execute("UPDATE table_exercise SET musclegrp=1, subgrp=3 WHERE eID=57")
# mycursor.execute("INSERT INTO table_exercise VALUES(60, 'WarmUp 10Min', 100, 100)")
# mycursor.execute("INSERT INTO table_exercise VALUES(61, 'Cardio 30Min', 101, 101)")
# mycursor.execute("INSERT INTO table_exercise VALUES(62, 'Cardio 25Min', 101, 101)")
# mycursor.execute("INSERT INTO table_exercise VALUES(63, 'Cardio 20Min', 101, 101)")
mycursor.execute("UPDATE table_exercise SET name='Schulterdruecken Maschine' WHERE eID=64")

mydb.commit()

#mycursor.execute("DROP TABLE table_subgrp")
#mycursor.execute("ALTER TABLE table_subgrp DROP COLUMN muscleGrp")
#mycursor.execute("ALTER TABLE table_subgrp DROP COLUMN musceGrp")
#mycursor.execute("ALTER TABLE table_subgrp ADD muscleGrp int")
#mycursor.execute("ALTER TABLE table_subgrp ADD CONSTRAINT FK_muscleGrpSub FOREIGN KEY (muscleGrp) REFERENCES table_muscleGrp(muscleGrp)");
#mycursor.execute("ALTER TABLE table_planex ADD reps tinyint")
#mycursor.execute("ALTER TABLE table_planex ADD sets tinyint")