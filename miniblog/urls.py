"""miniblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#import admin from django contributors
from django.contrib import admin
#import path and include from django urls
from django.urls import path, include
#import RedirectViews from django.views.generic to make it so you redirect the base url of the project to the url of the app through url maps
from django.views.generic import RedirectView
#import static to be able to use static files and images
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    #connects to urls for admin
    path('admin/', admin.site.urls),
    #connects to the urls in the blog app
    path('blog/', include('blog.urls')),
    #redirects base url of project to url of application. '' because if you do '/' you get a warning, set permanent to true so it happens no matter what
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]

#add a url path for static files/images
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
