"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.http import JsonResponse

# A simple fallback welcome view function
def home_index(request):
    return JsonResponse({"message": "Welcome to the E-Commerce API!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_index),  # <-- This safely catches the root homepage route
    # Your other e-commerce app routers go below...
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ecommerce.urls'))
]
