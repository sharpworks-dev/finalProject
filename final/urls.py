from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('forum/<int:id>', views.view_thread, name="thread"),
    path('post/<int:id>', views.view_post, name="post")
]