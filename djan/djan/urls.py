from django.contrib import admin
from django.urls import path
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('on/', views.on),
    path('writetopic/', views.writetopic),
    path('addtopic',views.result)
]
