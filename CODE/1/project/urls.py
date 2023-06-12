"""project URL Configuration

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
from .import views
from users import views as users_views
from admins import views as admins_views

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('user/', views.user, name='user'),


    # user's

    path('user_register/', users_views.UserRegisterActions, name='user_register'),
    path('user_login/', users_views.UserLoginCheck, name='user_login'),
    path('user_home/', users_views.UserHome, name='user_home'),
    path('user_logout/', users_views.logout, name='user_logout'),
    path('navie_bayes', users_views.navie_bayes, name='navie_bayes'),
    path('random_forest', users_views.random_forest, name='random_forest'),
    path('svm', users_views.svm, name='svm'),
    path('LR', users_views.logistic_regression, name='LR'),
    path('KNN', users_views.KNN, name='KNN'),
    path('DT', users_views.DT, name='DT'),
    path('predict', users_views.predict, name='predict'),

    # admin's
    path('admin_login/', admins_views.AdminLoginCheck, name='admin_login'),
    path('admin_home/', admins_views.AdminHome, name='admin_home'),
    path('logout/', admins_views.admin_logout, name='logout'),
    path('user_list/', admins_views.ViewRegisteredUsers, name='user_list'),
    path('user_activate/', admins_views.AdminActivaUsers, name='user_activate'),
]
