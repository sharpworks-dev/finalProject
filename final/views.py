from django.shortcuts import render, redirect
from .models import *
from .forms import ThreadForm, PostForm, CommentForm, UserForm, ProfileForm
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
    if request.method == "POST":
        form = request.POST.copy()
        user_id = request.user.id
        form.update({'user': user_id,
                     'post': id})
        final_comment_form = CommentForm(form)
        if final_comment_form.is_valid():
            final_comment_form.save()
            return redirect('post', id)

    comment_form = CommentForm()
    context = {'post': post,
               'author': author,
               'comments': comments,
               'commentForm': comment_form,
               'user_is_author': user_is_author}
    return render(request, 'final/view-post.html', context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
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


def create_post(request, thread_id):
    if request.method == 'POST':
        form = request.POST.copy()
        user_id = request.user.id
        form.update({'thread': thread_id,
                     'user': user_id})
        final_form = PostForm(form)
        if final_form.is_valid():
            post = final_form.save()
            return redirect('post', id=post.id)
    else:
        form = PostForm()

    thread = Thread.objects.get(id=thread_id)
    context = {'form': form, 'thread': thread}
    return render(request, 'final/create-post.html', context)


def view_profile(request, id):
    user_selected = User.objects.get(id=id)
    profile_selected = Profile.objects.get(user=user_selected.id)
    user_is_user_selected = request.user == user_selected
    context = {'user_selected': user_selected,
               'profile_selected': profile_selected,
               'user_is_user_selected': user_is_user_selected}
    return render(request, 'final/view-profile.html', context)


def edit_profile(request, id):
    user_selected = User.objects.get(id=id)
    profile_selected = Profile.objects.get(user=user_selected.id)
    user_is_user_selected = request.user == user_selected
    if user_is_user_selected:
        if request.method == "POST":
            user_form = UserForm(request.POST, instance=user_selected)
            profile_form = ProfileForm(request.POST, instance=profile_selected)
            if user_form.is_valid():
                user_form.save()
            if profile_form.is_valid():
                profile_form.save()
            return redirect('profile', user_selected.id)
        else:
            user_form = UserForm(instance=user_selected)
            profile_form = ProfileForm(instance=profile_selected)
            context = {'user_selected': user_selected,
                       'profile_selected': profile_selected,
                       'user_form': user_form,
                       'profile_form': profile_form}
            return render(request, 'final/edit-profile.html', context)
    else:
        return redirect('error')


def error_view(request):
    return render(request, 'final/403.html')
