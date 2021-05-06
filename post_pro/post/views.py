from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import Post
# Create your views here.

def post_list_and_create(request):
    qs = Post.objects.all()
    return render(request, 'post/main.html', {'qs':qs})

def load_post_data_view(request, num_post):
    visible = 3
    upper = num_post
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    data = []
    for obj in qs:
        item = {
            'id' : obj.id,
            'title': obj.title,
            'body': obj.body,
            'liked': True if request.user in obj.liked.all() else False,
            'author': obj.author.user.username, 
        }
        data.append(item)
    return JsonResponse({'data' : data[lower:upper], 'size': size})

def hello_world_view(request):
    return JsonResponse({'text': 'hello World'})