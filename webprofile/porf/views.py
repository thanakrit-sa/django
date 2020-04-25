from django.shortcuts import render
from django.db import models 
import datetime

def home(request):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    return render(request,'index.html',{'date':date})
