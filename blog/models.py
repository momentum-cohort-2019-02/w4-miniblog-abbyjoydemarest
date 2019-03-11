from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    """ Model representing a blog post."""


    #now define the fields that are needed for this class
    #set the title as a field
    title = models.CharField(max_length=100, null=True, blank=True)


    #the author is the blogger, so we assign it to be foreign key because we define blogger as a class later
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)


    #the post date must be set to the date that the blogger wrote the post
    post_date = models.DateField(null=True, blank=True)


    #the information that is in the blog
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        """ String to represent the Blog model object """
        return self.title

    
    def get_absolute_url(self):
        """ Gets the url for the detailed blog post """
        return reverse('blog-detail', args=[str(self.id)])



class Blogger(models.Model):
    """ Model representing the blogger (author of the blog who is a user). """
    username = models.CharField(max_length=150, null=True, blank=True)
    short_bio = models.TextField(verbose_name='Bio', null=True, blank=True)
    

    def __str__(self):
        """ String for representing the Blogger """
        return self.username


    def get_absolute_url(self):
        """ Gets the url for the  blogger details"""
        return reverse('blogger-detail', args=[str(self.id)])
