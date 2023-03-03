from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user_profile'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
    path('login/', views.loginViews, name='login_register'),
    path('logout/', views.logoutViews, name='logout'),
    path('register/', views.registerViews, name='register'),
    path('delete_message/<str:pk>/', views.deleteMessage, name='delete_message'),
    path('update_user/', views.updateUser, name='update_user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),


]