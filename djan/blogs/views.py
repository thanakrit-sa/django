from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import article
# from django.http import HttpResponse


def hello(request):
    data = article.objects.all()
    return render(request, 'index.html',{'post':data})


def on(request):
    return render(request, 'page1.html')


def writetopic(request):
    return render(request, 'writetopic.html')


def result(request):
    name = request.POST['nametopic']
    description = request.POST['description']
    return render(request, 'result.html', {'name': name, 'description': description})


def register(request):
    return render(request, 'register.html')


def member(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'มีชื่อผู้ใช้งานนี้อยู่ในระบบแล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'มีอีเมล์นี้อยู่ในระบบแล้ว')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password
            )
            user.save()
            return redirect('/')
    else:
        messages.info(request,'รหัสผ่านไม่ตรงกัน')
        return redirect('/register')

def showmember(request):
    return render(request,'member.html')

def login(request):
    return render(request,'login.html')

def loginform(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง')
        return redirect('/login')
