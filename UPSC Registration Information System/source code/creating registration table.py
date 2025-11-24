import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='computer',database='UPSC')
#if conn.is_connected():
      #print('connected sucessfully')
c1=conn.cursor()
#c1.execute("create table registration_information (name varchar(20)  ,father_name varchar(15),mother_name varchar(15),examination_applied varchar(40),year int(4),gender varchar(11),date_of_birth varchar(10),nationality varchar(15),marital_status varchar(10),community varchar(4),minority varchar(4),add_1 varchar(40),add_2 varchar(40),add_3 varchar(40),dist varchar(20),state varchar(20),pin_code int(6),pho_no int (10),mobile_no int (10),e_mail varchar(45),education_qualification varchar (100),preferance varchar(10),p_f_cds_pabt int (3),sainik_milt_sch int(3),son_sainik_mil_sch int (3),aadhar_no bigint)")
