from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("home.html")
@app.route('/cd',methods=['POST'])
def le():
    mail = request.form["i1"]
    pas = request.form["t7"]
    conn = mysql.connector.connect(host='localhost', user='root', db='regist' , password='')
    c = conn.cursor()
    c.execute("select * from regis where email='"+mail+"' and pwd='"+pas+"'")
    if(c.fetchone()):
        return render_template('Buy.html')
    else:
        return render_template('home.html')



@app.route('/about')
def abt():
    return render_template("/ABT.html")

@app.route('/contact')
def cnt():
    return render_template("contact.html")

@app.route('/feedback')
def feed():
    return render_template("feedback.html")
@app.route('/cod',methods=['POST'])    
def acti():
    e = request.form["in"]
    f = request.form["i"]
    l = request.form["ont"]
    c1 = request.form["c1"]
    c2 = request.form["c2"]
    c3 = request.form["c3"]
    name = request.form["name"]
    phone = request.form["phone"]
    mail = request.form["mail"]
    conn = mysql.connector.connect(host='localhost', user='root', db='regist' , password='')
    c = conn.cursor()
    c.execute("insert into regi(q1,q2,q3,c1,c2,c3,name,phone,mail) values('"+e+"','"+f+"','"+l+"','"+c1+"','"+c2+"','"+c3+"','"+name+"','"+phone+"','"+mail+"')")
    conn.commit()
    return render_template('home.html')
    

@app.route('/account')
def sub():

    return render_template("account.html")
@app.route('/code',methods=['POST'])
def act():
    email = request.form["t1"]
    fname = request.form["t2"]
    lname = request.form["t3"]
    uname = request.form["t4"]
    pwd = request.form["t5"]
    des = request.form["t6"]

    conn = mysql.connector.connect(host='localhost', user='root', db='regist' , password='')
    c = conn.cursor()
    c.execute("insert into regis(email,fname,lname,uname,pwd,des) values('"+email+"','"+fname+"','"+lname+"','"+uname+"','"+pwd+"','"+des+"')")
    conn.commit()
    return render_template('home.html')

@app.route('/live')
def lve():
    return render_template("live.html")

@app.route('/buy')
def by():
    return render_template("Buy.html")
@app.route('/list')
def lis():
    conn = mysql.connector.connect(host='localhost', user='root', db='regist' , password='')
    c = conn.cursor()
    c.execute("select * from regis")
    data=c.fetchall()
    return render_template("datab.html",data1=data)    

@app.route('/thankyou')
def thn():
    return render_template("thank.html")
    
if __name__ == '__main__':
    app.run()
