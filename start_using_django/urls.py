"""
URL configuration for start_using_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app01 import views

urlpatterns = [
    #   path('admin/', admin.site.urls),
    #   www.xxx.com/index/ -> 函数
    path('index/', views.index),
    path('users/user_list', views.user_list),
    path('users/user_del',views.user_del),
    path('tpl/',views.tpl),
    path('something/', views.something),
    path('login/',views.login),
    path('orm/test/',views.orm_test),

    #用户管理案例
    path('person/management/',views.person_management),
    path('person/add/', views.person_add),
    path('person/delete/', views.person_delete),
]
