"""
URL configuration for techsister_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.http import HttpResponse
from rest_framework.authtoken import views

def welcome(request):
    return HttpResponse("<h1>Welcome to TechSister AI API</h1><p>Go to <a href='/api/'>/api/</a> to view the API endpoints.</p>")

urlpatterns = [
    path('', welcome),  # 👈 add this line
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-token-auth/', views.obtain_auth_token), 
]
