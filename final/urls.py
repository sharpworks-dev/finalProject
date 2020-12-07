from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('thread/<int:id>', views.view_thread, name="thread"),
    path('create-thread/', views.create_thread, name="create-thread"),
    path('post/<int:id>', views.view_post, name="post"),
    path('create-post/<int:user_id>/<int:thread_id>', views.create_post, name="create-post")
]