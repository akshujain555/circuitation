import sqlite3  
  
con = sqlite3.connect("database.db")  
print("Database opened successfully")
con.execute("create table users (name text NOT NULL,username text NOT NULL,password text NOT NULL)")
#con.execute("create table cinpucon ( c1 DOUBLE NOT NULL, c2 DOUBLE  NOT NULL, c3 DOUBLE NOT NULL, c4 DOUBLE NOT NULL , va DOUBLE NOT NULL , T_hsa DOUBLE NOT NULL ,sign NUMBER NOT NULL ,regu NUMBER NOT NULL ,c NUMBER NOT NULL)")  
#con.execute("create table cinpuvar ( v1 NUMBER NOT NULL, v2 NUMBER  NOT NULL, v3 NUMBER NOT NULL , v4 NUMBER NOT NULL , v5 NUMBER NOT NULL, va number NOT NULL )")  


print("Table created successfully")  
  
con.close()  