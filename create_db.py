import mysql.connector


def create_db():
    con = mysql.connector.connect(
        host="localhost", user="root", passwd="minhhai2806", database="new_schema"
    )
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTO_INCREMENT,name text,duration text, charges text,description text)"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTO_INCREMENT,name text,email text,gender text,dob text,contact text,admission text,state text,city text,pin text,address text)"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTO_INCREMENT,roll text,name text, course text,marks_ob text, full_marks text, per text)"
    )
    con.commit()

    cur.execute(
        "Create table if not exists AllUsers(eid INTEGER primary key Auto_Increment,f_name text,l_name text, contact text, email text, question text, answer text, password text,u_name text)"
    )
    con.commit()

    con.close()


create_db()
