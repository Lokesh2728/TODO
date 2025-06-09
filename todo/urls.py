"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", list, name="list"),
    path("list", list, name="list"),
    path("add/", add, name="add"),
    path("edit/<int:id>/", edit, name="edit"),
    path("delete/<int:id>/", delete, name="delete"),
    path("complete/<int:id>/", complete, name="complete"),
    path("user_login/", user_login, name="user_login"),
    path("user_logout/", user_logout, name="user_logout"),
    path("user_regestration/", user_regestration, name="user_regestration"),
    
]
