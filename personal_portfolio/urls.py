"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include


"""This line of code includes all the URLs in the projects app but means they are accessed when prefixed by projects/. There are now two full URLs that can be accessed with our project:

localhost:8000/projects: The project index page
localhost:8000/projects/3: The detail view for the project with pk=3
These URLs still won’t work properly because we don’t have any HTML templates. But our views and logic are up and running so all that’s left to do is create those templates. If you want to check your code, take a look at the source code for this section."""

from django.contrib import admin
from django.urls import path, include
from django.urls import path
from personal_portfolio import views
from django.urls import path
from .views import Home  # Ensure this line is correct
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', views.Home.as_view(), name='home'),
    path('intro/', views.Intro.as_view(), name='intro'),
    path('dashboards/', views.Dashboards.as_view(), name='dashboards')
]


urlpatterns += staticfiles_urlpatterns()