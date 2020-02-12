
from django.contrib import admin
from django.urls import path
from lotto import views    # lotto폴더에서 views.py를 만들어줌

urlpatterns = [
    # 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/
    #path('',views.index),
    # 127.0.0.1:8000//hello/
    path('hello/', views.hello, name='hello_main'),
    # 127.0.0.1:8000//lotto/
    path('lotto/', views.index, name='index'),
    path('lotto/new', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail', views.detail , name='detail'),
]
