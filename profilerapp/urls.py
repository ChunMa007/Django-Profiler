from django.urls import path
from . import views

urlpatterns = [
    path('', views.getting_started, name='getting_started'),
    path('login/', views.user_login, name='user_login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
]
