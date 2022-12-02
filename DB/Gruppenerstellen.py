import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="AGM",
	passwd="1234",
	database="workautdb"
	)
	
mycursor = mydb.cursor()

# mycursor.execute("INSERT INTO table_group VALUES(1, 'Ganzkoerper Mann')")
# mycursor.execute("INSERT INTO table_group VALUES(2, 'Ganzkoerper Mann Cardio')")
# mycursor.execute("INSERT INTO table_group VALUES(3, '2er Split')")
# mycursor.execute("INSERT INTO table_group VALUES(4, 'Ganzkoerper Frau')")
# mycursor.execute("INSERT INTO table_group VALUES(5, 'Ganzkoerper Frau Cardio')")
# mycursor.execute("INSERT INTO table_group VALUES(6, 'Bauch, Beine, Po')")
# mycursor.execute("INSERT INTO table_group VALUES(7, 'Bauch, Beine, Po - Cardio')")

# mycursor.execute("INSERT INTO table_plangroup VALUES(1, 1, 1)")
# mycursor.execute("INSERT INTO table_plangroup VALUES(2, 2, 3)")
# mycursor.execute("INSERT INTO table_plangroup VALUES(3, 3, 5)")
# mycursor.execute("INSERT INTO table_plangroup VALUES(4, 3, 6)")
# mycursor.execute("INSERT INTO table_plangroup VALUES(5, 4, 2)")
# mycursor.execute("INSERT INTO table_plangroup VALUES(6, 5, 4)")
# mycursor.execute("INSERT INTO table_plangroup VALUES(7, 6, 7)")
# mycursor.execute("INSERT INTO table_plangroup VALUES(8, 6, 2)")
mycursor.execute("INSERT INTO table_plangroup VALUES(9, 7, 4)")
mycursor.execute("INSERT INTO table_plangroup VALUES(10, 7, 7)")

mydb.commit()

#Mann -> gpID, gID, gender, goal, tpw
mycursor.execute("INSERT INTO table_assign VALUES(1, 1, 1, 'Aufbau', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(2, 1, 1, 'Fitter werden', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(3, 1, 1, 'Aufbau', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(4, 1, 1, 'Fitter werden', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(5, 1, 1, 'Fitter werden', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(6, 2, 1, 'Abnehmen', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(7, 2, 1, 'Fitter werden', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(8, 2, 1, 'Abnehmen', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(9, 2, 1, 'Fitter werden', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(10, 2, 1, 'Abnehmen', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(11, 2, 1, 'Fitter werden', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(12, 2, 1, 'Fitter werden', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(13, 3, 1, 'Aufbau', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(14, 3, 1, 'Aufbau', 4)")
mycursor.execute("INSERT INTO table_assign VALUES(15, 3, 1, 'Fitter werden', 4)")
#Frau -> gpID, gID, gender, goal, tpw
mycursor.execute("INSERT INTO table_assign VALUES(16, 4, 0, 'Aufbau', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(17, 4, 0, 'Fitter werden', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(18, 4, 0, 'Aufbau', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(19, 4, 0, 'Fitter werden', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(20, 4, 0, 'Fitter werden', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(21, 5, 0, 'Abnehmen', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(22, 5, 0, 'Fitter werden', 1)")
mycursor.execute("INSERT INTO table_assign VALUES(23, 5, 0, 'Fitter werden', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(24, 5, 0, 'Abnehmen', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(25, 5, 0, 'Abnehmen', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(26, 5, 0, 'Fitter werden', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(27, 6, 0, 'Aufbau', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(28, 6, 0, 'Fitter werden', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(29, 6, 0, 'Fitter werden', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(30, 7, 0, 'Abnehmen', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(31, 7, 0, 'Fitter werden', 2)")
mycursor.execute("INSERT INTO table_assign VALUES(32, 7, 0, 'Abnehmen', 3)")
mycursor.execute("INSERT INTO table_assign VALUES(33, 7, 0, 'Fitter werden', 3)")

mydb.commit()