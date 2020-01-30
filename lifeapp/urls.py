"""lifeStyleblog URL Configuration

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

from django.urls import path
from .import views
from django.contrib.sitemaps.views import sitemap
from .views import  articleSitemap

sitemaps = {
    'article': articleSitemap,
}

urlpatterns = [
    path('', views.index, name="index"),
    path('Life', views.life, name="Life"),
    path('Contact',views.Contact, name="Contact"),
    path('topic/<name>', views.blog, name="topic"),
    path('article/<slug:slug_text>', views.blogger, name="blog2"),
    path('author/<name>',views.getauthor,name="author"),
    path('search', views.search, name="search"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')

]
