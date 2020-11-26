from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    threads = Thread.objects.all()
    context = {'threads': threads}
    return render(request, 'final/test.html', context)


def view_thread(request, id):
    posts = Post.objects.filter(thread_id=id)
    context = {'posts': posts}
    return render(request, 'final/view-thread.html', context)

def view_post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post_Id=id)
    context = {'post': post, 'comments': comments}
    return render(request, 'final/view-post.html', context)
