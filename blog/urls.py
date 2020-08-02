"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    path('cse', views.cse, name = 'cse'),
    path('ece', views.ece, name = 'ece'),
    path('eec', views.eec, name = 'eec'),
    path('user_setting', views.user_setting, name = 'user_setting'),
    path('notice', views.notice, name = 'notice'),
    path('write', views.write, name = 'write'),
    path('save_notice', views.save_notice, name = 'save_notice'),
    path('blog/<int:blog_id>', views.show_notice, name = 'show_notice'),
    path('user_setting/<int:user_id>', views.delete_user, name = 'delete_user'),
]
