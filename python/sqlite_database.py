import sqlite3 as sq
con=sq.connect("mydatabase.txt")
cur=con.cursor()

# create table
cur.execute("create table if not exists student(id int,name text)")

##insert data into table
# cur.execute("insert into student(id,name) values(?,?)",(1,'Abc')) 

# insert many values
hello=[(1,'shiv'),(2,"gaju"),(3,"gaurav"),(4,"Arjun")]
cur.executemany("insert into student values(?,?)",hello) 

# drop database
# cur.execute("DROP TABLE student")

# # retrive data from database
# data=cur.execute("select * from student")
# for row in data:
#     print(row[0])   # print first line
#     print(row)    # print all lines

# fetchall=> print all data
cur.execute("select * from student")
data=cur.fetchall()
for row in data:
    print(row)

# # fetchone => fetch one data and print
# cur.execute("select * from student where id=?",[2])   
# data=cur.fetchone()  # fetchone data only
# print(data)

# # to update values
# cur.execute("update student set name='devil'where id=2")

# # delete particular values
# cur.execute("delete from student where id=2 ")

# # delete all at once
# cur.execute("delete from student")

con.commit()
con.close()
