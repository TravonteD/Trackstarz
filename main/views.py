from django.http import JsonResponse
from django.core import serializers
from .models import User

# User Methods
def user_index(request):
    data = list(map(format_user, User.objects.all()))
    return JsonResponse({'data': data})

def user_show(request, pk):
    data = format_user(User.objects.get(pk=pk))
    return JsonResponse(data)

def format_user(user):
    return {
            'id': user.id,
            'username': user.username,
            'displayname': user.displayname,
            'email': user.email,
            'startdate': user.startdate,
            'about': user.about,
            'birthdate': user.birthdate,
            'youtube': user.youtube,
            'twitter': user.twitter,
            'instagram': user.instagram,
            'pinterest': user.pinterest,
            'website': user.website,
            'created_at': user.created_at,
            'updated_at': user.updated_at
            }

# Post Methods
def post_index(request):
    data = list(map(format_post, Post.objects.all()))
    return JsonResponse({'data': data})

def post_show(request, pk):
    data = format_post(Post.objects.get(pk=pk))
    return JsonResponse(data)

def format_post(post):
    return {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at,
            'updated_at': post.updated_at
            }

# Comment Methods
def comment_index(request):
    data = list(map(format_comment, Comment.objects.all()))
    return JsonResponse({'data': data})

def comment_show(request, pk):
    data = format_comment(Comment.objects.get(pk=pk))
    return JsonResponse(data)

def format_comment(comment):
    return {
            'id': comment.id,
            'content': comment.content,
            'created_at': comment.created_at,
            'updated_at': comment.updated_at
            }
