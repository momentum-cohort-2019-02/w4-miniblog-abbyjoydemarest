#bring in render from shortcuts in Django so you can output information that was requested
from django.shortcuts import render
#brings in the Blog and Blogger classes from models.py so you can use that information
from blog.models import Blog, Blogger
#bring in generic from Django's views so you can ask it(query) to get all records of the above models.
from django.views import generic
# Create your views for the blog app here.

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


class BlogListView(generic.ListView):
    model = Blog
    queryset = Blog.objects.order_by('-post_date')
