from django.shortcuts import render, redirect
from .models import *
from .forms import ThreadForm, PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    threads = Thread.objects.all()
    context = {'threads': threads}
    return render(request, 'final/home.html', context)


def view_thread(request, id):
    thread = Thread.objects.get(id=id)
    posts = Post.objects.filter(thread_id=id)
    context = {'thread': thread, 'posts': posts}
    return render(request, 'final/view-thread.html', context)


def view_post(request, id):
    post = Post.objects.get(id=id)
    author_id = post.user_id
    author = User.objects.get(id=author_id)
    comments = Comment.objects.filter(post_id=id)
    user_is_author = request.user == author
    context = {'post': post, 'author': author, 'comments': comments, 'user_is_author': user_is_author}
    return render(request, 'final/view-post.html', context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
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


def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save()
            return redirect('thread', id=thread.id)
    else:
        form = ThreadForm()

    context = {'form': form}
    return render(request, 'final/create-thread.html', context)


def create_post(request, user_id, thread_id):
    if request.method == 'POST':
        form = request.POST.copy()
        form.update({'thread_id': thread_id,
                     'user_Id': user_id})
        final_form = PostForm(form)
        if final_form.is_valid():
            post = final_form.save()
            return redirect('post', id=post.id)
    else:
        form = PostForm()

    thread = Thread.objects.get(id=thread_id)
    context = {'form': form, 'thread': thread}
    return render(request, 'final/create-post.html', context)
