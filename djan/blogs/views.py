from django.shortcuts import render
from django.contrib.auth.models import User
# from django.http import HttpResponse


def hello(request):
    return render(request,'index.html')


def on(request):
    return render(request, 'page1.html')

def writetopic(request):
    return render(request,'writetopic.html')

def result(request):
    name = request.POST['nametopic']
    description = request.POST['description']
    return render(request,'result.html',{'name':name,'description':description})

def register(request):
    return render(request,'register.html')

def member(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    user = User.objects.create_user(
        username =username,
        first_name =firstname,
        last_name =lastname,
        email =email,
        password =password
    )
    user.save()
    return render(request,'member.html')