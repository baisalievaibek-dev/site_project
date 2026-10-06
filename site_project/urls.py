"""
URL configuration for site_project project.

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('hudozhestvennaya/', views.hudoj_literatura, name='hudoj_literatura'),
    path('biznes/', views.business_books, name='business_books'),
    path('istoriya/', views.history_books, name='history_books'),
    path('psihologiya/', views.psychology_books, name='psychology_books'),
    path('nauka/', views.science_books, name='science_books'),
]
