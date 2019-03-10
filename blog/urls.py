#import path from django.urls
from django.urls import path
#import the views from this directory
from . import views

urlpatterns = [
    #create the url path for the index page for the application
    path('', views.index, name='index'),
]
