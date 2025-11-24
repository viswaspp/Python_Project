import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='computer',database='UPSC')
#if conn.is_connected():
      #print('connected sucessfully')
c1=conn.cursor()
#v_sql=("create table login_info (user varchar(10) primary key, pass varchar(10)) ")
#print(v_sql)
#c1.execute(v_sql)
us=input("user")
pa=input("pass")
v_sq=("insert into login_info values('"+us+"','"+pa+"')")
print(v_sq)
c1.execute(v_sq)
conn.commit()
