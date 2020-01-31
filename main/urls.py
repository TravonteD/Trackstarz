from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('users/', views.user_index, name='user-index'),
    path('users/<int:pk>/', views.user_show, name='user-show'),
    path('users/new/', views.user_new, name='user-new'),
    path('users/edit/<int:pk>/', views.user_edit, name='user-edit'),
    path('users/delete/<int:pk>/', views.user_delete, name='user-delete'),
    path('posts/', views.user_index, name='post-index'),
    path('posts/<int:pk>/', views.user_show, name='post-show'),
    path('comments/', views.user_index, name='comment-index'),
    path('comments/<int:pk>/', views.user_show, name='comment-show')
]
