from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ex: John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ex: Wick'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ex: jwick@fortnite.com'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'bio': forms.Textarea(),
            'status': forms.TextInput(),
            'user': forms.HiddenInput()
        }


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter thread name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your thread'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'body': forms.Textarea(attrs={'placeholder': 'Type out your post here'}),
            'thread': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a comment'}),
            'post': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }