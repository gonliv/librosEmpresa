"""
URL configuration for resena_libros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from librosApp.views import index, contact, success, login_view, welcome, register_view, custom_logout_view, profile_view, library_view, book_detail_view, book_creation_view
from django.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= "index"),
    path("contact/", contact, name= "contact"),
    path("success/", success, name= "success"),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path("welcome/", welcome, name= "welcome"),
    path('password_change/', include('django.contrib.auth.urls'), name='password_change'),
    path('password_change/done/', include('django.contrib.auth.urls'), name='password_change_done'),
    path('password_reset/', include('django.contrib.auth.urls'), name='password_reset'),
    path('password_reset/done/', include('django.contrib.auth.urls'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', include('django.contrib.auth.urls'), name='password_reset_confirm'),
    path('reset/done/', include('django.contrib.auth.urls'), name='password_reset_complete'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('library/', library_view, name='library'),
    path('book_detail/<int:pk>/', book_detail_view, name='book_detail'),
    path('book_creation/', book_creation_view, name='book_creation'),   
    
]
