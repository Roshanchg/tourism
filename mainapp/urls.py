from django.contrib import admin
from django.urls import path
from mainapp import views
app_name='mainapp'
urlpatterns = [
    path('',views.mainPage,name="index"),
    path('login',views.loginForm,name="login"),
    path('register',views.registerForm,name="register"),
    path('account/<str:email>',views.myaccount,name='myaccount'),
]
