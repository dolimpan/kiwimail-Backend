# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
]

'''
/Users/pado/Documents/postbox/postbox'''