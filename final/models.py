from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.first_name + " \"" + self.username + "\" " + self.last_name


class Thread(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " -- " + self.description


class Post(models.Model):
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=10000)

    def __str__(self):
        return "User: " + str(self.user_Id.username) + " -- " + self.title


class Comment(models.Model):
    post_Id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return "User: " + str(self.user_Id.username) + " -- " + self.body
