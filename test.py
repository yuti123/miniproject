
import sqlite3

def insertdb(id, Name):
	conn = sqlite3.connect('face.db')
	cmd="SELECT * FROM PERSON WHERE id="+str(Id)
	cursor=conn.execute(cmd)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if (isRecordExist==1):
		cmd="UPDATE PERSON SET name="+str(Name)+"WHERE id="+str(id)
	else:
		cmd="INSERT INTO  PERSON (id, na0me) values ("+str(Name)+","+str(id)+")"

	conn.execute(cmd)
	conn.commit()
	conn.close()

id=int (input("enter your id"))
Name=str(input("Enter your name "))
insertdb(id,Name)