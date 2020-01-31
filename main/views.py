import json
from django.core import serializers, validators
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import User

# User Methods
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'data': {
            'id': request.session.get('_auth_user_id'),
            'token': request.session.get('_auth_user_hash')
            }})
    else:
        return JsonResponse({"errors": "invalid credentials"})

def user_index(request):
    data = list(map(format_user, User.objects.all()))
    return JsonResponse({"data": data})

def user_show(request, pk):
    data = format_user(User.objects.get(pk=pk))
    return JsonResponse(data)

def user_new(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username=username,email=email)
        user.set_password(password)
        User.clean_fields(user)
    except Exception as e:
        response = JsonResponse({"errors": e.message_dict})
        response.status_code = 400
        return response
    data = format_user(user)
    return JsonResponse({"data": data })

def user_edit(request, pk):
    user = User.objects.filter(pk=pk)
    if len(user) != 0:
        user.update(**json.loads(request.body))
        try:
            User.clean_fields(user[0])
        except ValidationError as e:
            response = JsonResponse({"errors": e.message_dict})
            response.status_code = 400
            return response
        data = format_user(user[0])
        return JsonResponse({"data": data })
    else:
        response = JsonResponse({"errors": "invalid id given"})
        response.status_code = 400
        return response

def user_delete(request, pk):
    result = User.objects.filter(id=pk).delete()
    if result[0] != 0:
        return JsonResponse({"data": result[1]})
    else:
        response = JsonResponse({"errors": "invalid id given"})
        response.status_code = 400
        return response


def format_user(user):
    return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'displayname': user.profile.displayname,
            'startdate': user.profile.startdate,
            'about': user.profile.about,
            'birthdate': user.profile.birthdate,
            'youtube': user.profile.youtube,
            'twitter': user.profile.twitter,
            'instagram': user.profile.instagram,
            'pinterest': user.profile.pinterest,
            'website': user.profile.website,
            'created_at': user.profile.created_at,
            'updated_at': user.profile.updated_at
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

