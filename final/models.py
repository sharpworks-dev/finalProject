from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000)
    status = models.CharField(max_length=30)


class Thread(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " -- " + self.description


class Post(models.Model):
    thread = models.ForeignKey(Thread, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=10000)

    def __str__(self):
        return "User: " + str(self.user.username) + " -- " + self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return "User: " + str(self.user_Id.username) + " -- " + self.body
