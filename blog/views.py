from django.shortcuts import render
from blog.models import Blog, Blogger
# Create your views here.

def index(request):
    """This is the view function for the homepage/index page of the site."""


    #Generate counts of the main objects so people can see what the website contains
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()


    #create the context to be displayed later
    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
    }


    #render the html template  index.html with the context data
    return render(request, 'index.html', context=context)
