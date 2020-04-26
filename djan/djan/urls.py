from django.contrib import admin
from django.urls import path
from blogs import views
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('on/', views.on),
    path('writetopic/', views.writetopic),
    path('addtopic',views.result),
    path('register/',views.register),
    path('addmember',views.member),
    path('member',views.showmember),
    path('login',views.login),
    path('loginform',views.loginform)
]