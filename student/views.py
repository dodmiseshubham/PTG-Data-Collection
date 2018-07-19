from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.template import loader
from .models import Student
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
import pymysql.cursors

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'a.html')

def search(request):
    return render(request, 'a.html')

def search(request):
    connection = pymysql.connect(host='localhost',
                                 user='dodmise',
                                 password='dodmise123',
                                 db='dbms',
                                 )
    if request.method == 'POST':
            form = (request.POST)

            s1 = form['erp']
            s2 = form['roll']
            a1=[]
            try:

                with connection.cursor() as cursor:
                    sql = "SELECT * from `form1` where `Student_ID_:`=(%s)"
                    cursor.execute(sql, (s1))
                    a = cursor.fetchone()
                    if(a==None):
                        return render(request,"nomatch.html")
                    d = {}
                    d['a'] = a[0]
                    d['b'] = a[1]
                    d['c'] = a[2]
                    d['d'] = a[3]
                    d['e'] = a[4]
                    d['f'] = a[5]
                    d['g'] = a[6]
                    d['h'] = a[7]
                    d['i'] = a[8]
                    d['j'] = a[9]
                    d['k'] = a[10]
                    d['l'] = a[11]
                    d['m'] = a[12]
                    return render(request, "search.html", {"d": d, })
            finally:
                connection.close()

def teacher(request):
  connection = pymysql.connect(host='localhost',
                                 user='dodmise',
                                 password='dodmise123',
                                 db='dbms',
                                 )
  if request.method == 'POST':
   form = (request.POST)

   s1 = form['teach']
   s2 = form['passw']
   a1 = []

   try:
        a = []
        b = []
        c = []
        d = []
        with connection.cursor() as cursor:
            sql = "SELECT * from `teacher` where `teach_name`=(%s) and `pass`=(%s)"
            cursor.execute(sql, (s1,s2))
            a1 = cursor.fetchone()
            if (a1 == None):
                return render(request, "nomatch.html")
            sql1 = "SELECT * from `form1`"
            cursor.execute(sql1)
            result = cursor.fetchall()
            for i in result:
                d={}
                d['a'] = i[0]
                d['b'] = i[1]
                d['c'] = i[2]
                d['d'] = i[3]
                d['e'] = i[4]
                d['f'] = i[5]
                d['g'] = i[6]
                d['h'] = i[7]
                d['i'] = i[8]
                d['j'] = i[9]
                d['k'] = i[10]
                d['l'] = i[11]
                d['m'] = i[12]
                a.append(d)
            return render(request, "teach.html", {"a": a, })
   finally:
        connection.close()