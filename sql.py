import mysql.connector
cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="395F844E696D423F6B7ACBBA301539668E6",
  port= 3306,
  database="alprdata"
)

cursor = cnx.cursor(dictionary=True)

cursor.execute("SELECT * FROM plates")
