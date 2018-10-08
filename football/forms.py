from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from football.models import Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='optional')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
