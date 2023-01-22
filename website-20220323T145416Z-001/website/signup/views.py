from django.shortcuts import render
import mysql.connector as mysql
fn=''
ln=''
s=''
em=''
pwd='' 
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        mydb = mysql.connect(user="root", host="localhost", passwd="Yadav@2922", database="loginnn",
                                       auth_plugin="mysql_native_password")

        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into userss Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        mydb.commit()

    return render(request,'signup_page.html')
