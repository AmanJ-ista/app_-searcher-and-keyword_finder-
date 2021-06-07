"""Highbreed URL Configuration

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
from django.urls import path
from development.views import Home 
from development import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view()),
    path('app_searcher',views.app,name='app_searcher'),
    path('myapp',views.google_app,name='google_app'),
    path('myapp2',views.apple_app,name='apple_app'),
   
    path('keyword_finder',views.keyword_find,name='keyword_finder'),
    path('finder',views.keyword_finder,name='keyword'),

]
