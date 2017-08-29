# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
import random
from InfoModel.models import *


# Create your views here.
from django.core.context_processors import csrf

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

@csrf_exempt
def search_form(request):
    return render_to_response('search_form.html')

@csrf_exempt
def search(request):
    authors = Author.objects.all()
    if request.GET['name']:
        authors = authors.filter(name=request.GET['name'])
    if request.GET['sex']:
        authors = authors.filter(sex=request.GET['sex'])
    if request.GET['age']:
        authors = authors.filter(age=request.GET['age'])
    if request.GET['email']:
        authors = authors.filter(email=request.GET['email'])
    return render_to_response('search_results.html',{'authors': authors})
    
@csrf_exempt
def searchbook_form_bo(request):
    return render_to_response('searchbook_form_bo.html')

@csrf_exempt
def booksearch_bo(request):
    if request.GET['author']:
        books = Book.objects.filter(author=request.GET['author'])
    if request.GET['title']:
        books = Book.objects.filter(title=request.GET['title'])
    if request.GET['publisher']:
        books = Book.objects.filter(publisher=request.GET['publisher'])
    if request.GET['date']:
        books = Book.objects.filter(date=request.GET['date'])
    return render_to_response('booksearch_result_bo.html',{'books': books})

#访问首页
def add(request):
    return render_to_response('add.html')
    
def addbook(request):
    return render_to_response('addbook.html')

#保存数据
@csrf_exempt
def submit(request):
    name=request.POST['name']
    sex=request.POST['sex']
    age=request.POST['age']
    address=request.POST['email']
    try: #不能与现有的主键重复
        au = Author.objects.get(email = address)
        html = "<html><body>The key has already existed.</body></html>"
        return HttpResponse(html)
    except:
        au=Author()
        au.name = name
        au.sex = sex
        au.age = age
        au.email = address
        au.save()
        return HttpResponseRedirect("/display/")

@csrf_exempt
def submitbook(request):
    title=request.POST['title']
    author=request.POST['author']
    publisher=request.POST['publisher']
    date=request.POST['date']
    bo = Book()
    bo.title = title
    bo.author = author
    bo.publisher = publisher
    bo.date = date
    bo.save()
    book = Book.objects.filter(author = author)
    return render_to_response('seebook.html',{'data': book})
        
def display(request):
    au = Author.objects.all()
    return render_to_response('display.html', {'data':au})
    
def seebook(request):
    id = request.GET['id']
    au = Author.objects.get(id = id)
    books = Book.objects.filter(author = au.name)
    return render_to_response('seebook.html', {'data':books})
    
def seeallbook(request):
    bo=Book.objects.all()
    return render_to_response('seebook.html', {'data':bo})
    
def back(request):
    au = Author.objects.all()
    return render_to_response('display.html', {'data':au})
    
#删除数据
def delByauthor(request):
    id = request.GET['id'];
    bb = Author.objects.get(id = id)
    bb.delete()
    return HttpResponseRedirect("/display")

def delBybook(request):
    id = request.GET['id'];
    bb = Book.objects.get(id = id)
    author = bb.author
    bb.delete()
    if author:
        book = Book.objects.filter(author = author)
        return render_to_response('seebook.html', {'data':book})
    else:
        book = Book.objects.all()
        return render_to_response('seebook.html', {'data':book})

def pack_modify(request):
    id = request.GET['id'];
    name = request.GET['name']
    sex = request.GET['sex']
    age = request.GET['age']
    email = request.GET['email']
    return render_to_response('modify.html', {'data':{'id': id, 'name': name, 'sex': sex, 'age': age, 'email': email}})
    
def pack_modify_bo(request):
    id=request.GET['id'];
    return render_to_response('bo_modify.html', {'id': id})

@csrf_exempt    
def modify(request):
    id=request.GET['id'];
    au = Author.objects.get(id = id)
    name=request.POST['name']
    sex=request.POST['sex']
    age=request.POST['age']
    address=request.POST['email']
    au.name = name
    au.sex = sex
    au.age = age
    au.email = address
    au.save()
    return HttpResponseRedirect("/display/") 

@csrf_exempt
def changebook(request):
    id=request.GET['id'];
    bo = Book.objects.get(id = id) 
    author=request.POST['author']
    title=request.POST['title']
    publisher=request.POST['publisher']
    date=request.POST['date']
    bo.author = author
    bo.title = title
    bo.publisher = publisher
    bo.date = date
    bo.save()
    book = Book.objects.filter(author = author)
    return render_to_response('seebook.html', {'data':book})

'''
def myhtml(request):
    return render_to_response('a.html',locals())


def bb(request):
    return render(request,'bb.html')
    



    
#保存数据
@csrf_exempt
def add(request):
    # c={}
    id=request.POST['id']
    name=request.POST['name']
    age=request.POST['age']
    st=Student()
    if len(id) > 0 :
        print("id不是null")
        st.id=id;
    st.age=age
    st.name=name
    st.save()
    return HttpResponseRedirect("/q")

#查询所有

    

#显示一条数据
def showUid(request):
    id=request.GET['id'];
    bb=Student.objects.get(id=id)
    return render_to_response('update.html',{'data':bb})
    

#删除数据
def delByID(request):
    id=request.GET['id'];
    bb=Student.objects.get(id=id)
    bb.delete()
    return HttpResponseRedirect("/q")

datas=[

    {"id":"1","name":"华为"},
    {"id":"2","name":"三星"},
    {"id":"4","name":"Apple"},
    {"id":"5","name":"中国"},
    {"id":"6","name":"JAVA程序员"},
    {"id":"7","name":"solr"},
    {"id":"8","name":"hadoop编程"},
    {"id":"9","name":"python"},

]

def show(request):
        return render_to_response('data.html',{'datas':datas})
'''
