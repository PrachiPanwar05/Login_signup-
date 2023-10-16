from django.shortcuts import render
import mysql.connector as mysql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        mydb=mysql.connect(host="localhost",user="root",passwd="0522",database='loginnn',auth_plugin="mysql_native_password")
        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')
