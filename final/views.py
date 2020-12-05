from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    threads = Thread.objects.all()
    context = {'threads': threads}
    return render(request, 'final/home.html', context)


def view_thread(request, id):
    posts = Post.objects.filter(thread_id=id)
    context = {'posts': posts}
    return render(request, 'final/view-thread.html', context)


def view_post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post_Id=id)
    context = {'post': post, 'comments': comments}
    return render(request, 'final/view-post.html', context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'final/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'final/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')
