from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_index),
    path('users/<int:pk>/', views.user_show),
    path('posts/', views.user_index),
    path('posts/<int:pk>/', views.user_show),
    path('comments/', views.user_index),
    path('comments/<int:pk>/', views.user_show)
]
