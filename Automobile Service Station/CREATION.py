import mysql.connector as sql 
conn=sql.connect(host='localhost',user='root',passwd='manager',database='AUTO_MOBILE_SURVICE_STATION')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create table customer_details((sno int primary key, cname varchar(25),cdetails varchar(30),caddress varchar(30),cpincode int,cpuramt int,cdisc float)')

print ('table created')
