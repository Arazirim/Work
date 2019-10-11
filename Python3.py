import sqlite3

	rows=[]

	rows2=[]

	conn = sqlite3.connect('Chinook_Sqlite.sqlite')

	cursor = conn.cursor()

	for x in cursor.execute("SELECT  * FROM outlets "):
		rows.append(x)

# Дедупликация
	for x in rows:

		for y in rows:
			
			if x[1]==y[1] and x[2]==y[2] and x[3]==y[3] and x[0]!=y[0] :
				
				rows.remove(y)


	rows1=set(rows)

	try:
		cursor.executemany("Insert into outlets_clean (`Город дистрибьютора`,`Торг_точка_чистая`,`Торг_точка_чистая_адрес`,old_id) values (?,?,?,?)",((x[1],x[2],x[3],x[0],) for x in rows1))
		result = cursor.fetchall()
	except sqlite3.DatabaseError as err:       
		print("Error: ", err)
	else:
		    conn.commit()

	for x in cursor.execute("SELECT  * FROM outlets_clean "):
		rows2.append(x)

	try:
		cursor.executemany("UPDATE outlets SET outlet_clean_id = ? WHERE id  = ?",((x[0],x[4]) for x in rows2))
		result = cursor.fetchall()
	except sqlite3.DatabaseError as err:       
		print("Error: ", err)
	else:
		    conn.commit()


conn.close()