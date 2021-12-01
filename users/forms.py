from django import forms
from .models import UserModel, Posts


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=225, widget=forms.TextInput(
        attrs={'placeholder': 'FirstName'}))
    last_name = forms.CharField(max_length=225, widget=forms.TextInput(
        attrs={'placeholder': 'LastName'}))
    username = forms.CharField(max_length=225, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=225, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    email = forms.EmailField(max_length=225, widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}
    ))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email')


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('text',)
