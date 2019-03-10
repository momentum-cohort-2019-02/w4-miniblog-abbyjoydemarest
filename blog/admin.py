from django.contrib import admin
from blog.models import Blog, Blogger

admin.site.register(Blog)
admin.site.register(Blogger)

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'description')
    fields = ['title', 'author', 'post_date', 'description']
    
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('username', 'bio')
    fields = ['username', 'short_bio']
    