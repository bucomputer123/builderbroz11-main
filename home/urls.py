
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
     path('',views.index,name='home'),
     path('about/',views.about,name='about'),
     path('services/',views.services,name='services'),
     path('contact/',views.contact,name='contact'),
     path('donate/',views.donate,name='donate'),
     # path('download/',views.download,name='download'),
     url(r'^$', views.index, name='home'),
     url(r'^download/', views.download, name='download')
    
]
