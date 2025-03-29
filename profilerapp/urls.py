from django.urls import path
from . import views

urlpatterns = [
    path('', views.getting_started, name='getting_started'),
    path('login/', views.user_login, name='user_login'),
    path('home/', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('view_profile/<str:username>', views.view_profile, name="view_profile"),
    path('edit_profile/<str:username>', views.edit_profile, name="edit_profile"),
    path('delete_profile/<str:username>', views.delete_profile, name="delete_profile"),
]
