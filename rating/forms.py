from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Detail

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_author', 'post_caption', 'post_img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['post_caption'].widget.attrs['placeholder'] = 'Write caption...'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'Firstname'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Lastname'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'post_caption', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['text'].widget.attrs['placeholder'] = 'Write comment...'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['first_name', 'last_name', 'username', 'email', 'img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'Firstname'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Lastname'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'Firstname'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Lastname'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

