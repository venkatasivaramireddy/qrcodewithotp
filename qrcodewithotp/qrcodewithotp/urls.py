"""qrcodewithotp URL Configuration

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
from django.contrib import admin
from django.urls import path,include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('register_details/',views.register_details,name="register_details"),
    path('login_page/',views.login_page,name="login_page"),
    path('validate_login/',views.validate_login,name='validate_login'),
    path('otpvalidation/',views.otpvalidation,name='otpvalidation'),

    path('account/',include("allauth.urls"))
]
