from django import forms
from django.contrib.auth.models import User
from blog.models import Category, Post, UserProfile, Comment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]