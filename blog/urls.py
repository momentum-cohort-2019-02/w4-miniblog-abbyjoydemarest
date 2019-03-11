#import path from django.urls
from django.urls import path
#import the views from this directory
from . import views

#this page houses the url paths for this app

urlpatterns = [
    #create the url path for the index page for the application
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggersListView.as_view(), name='bloggers'),
]
