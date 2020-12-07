from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'bio': forms.Textarea(),
            'status': forms.TextInput()
        }


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter thread name.'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your thread.'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title.'}),
            'body': forms.Textarea(attrs={'placeholder': 'Type out your post here.'}),
            'thread_id': forms.HiddenInput(),
            'user_Id': forms.HiddenInput()
        }
