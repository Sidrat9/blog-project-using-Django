from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello, Django!</h1>')

# def post_list(request):
#     posts = Post.objects.all()
#     result = ""
#     for post in posts:
#         result += post.title + "</br>"
#     print(result)
#     return HttpResponse(result)

def post_list(request):
    posts = Post.objects.all()
    context = { 
        "name": "Munatah",
        "posts": posts
    }
    return render(request, 'post_list.html',context ) # html include er khetre render use korte hobe

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return HttpResponse("<h1>post detail!</h1>")