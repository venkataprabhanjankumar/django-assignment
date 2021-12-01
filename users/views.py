from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from .forms import RegisterForm, LoginForm, ProfileForm, PostForm
from .models import UserModel, Posts


def default_url(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return redirect('/login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = UserModel.objects.get(username=form.cleaned_data['username'])
                return render(request, 'register.html',
                              {'form': form, 'menu': 'register', 'fail': 'User Already Exists With username'})
            except UserModel.DoesNotExist:
                user = UserModel.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                login(request, user)
                messages.success(request, _('Account created'))
                return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'form': form, 'menu': 'register'})
    else:
        form = RegisterForm()
        return render(request, 'login.html', {'form': form, 'menu': 'register'})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request=request, user=user)
                return redirect('/dashboard')
            else:
                return render(request, 'login.html',
                              {'form': form, 'menu': 'login', 'fail': 'Invalid Username Or Password'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form, 'menu': 'login'})


@login_required(login_url='/login')
def dashboard(request):
    user = UserModel.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = ProfileForm(instance=user, data=request.POST)
        form.save()
        return redirect('/dashboard')
    else:
        form = ProfileForm(instance=user)
        return render(request, 'dashboard.html', {'username': request.user.username, 'form': form})


@login_required(login_url='/login')
def new_post(request):
    user = UserModel.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('/posts')
    else:
        form = PostForm()
        return render(request, 'new_post.html', {'form': form})


@login_required(login_url='/login')
def user_posts(request):
    user = UserModel.objects.get(username=request.user.username)
    posts = Posts.objects.filter(user=user)
    return render(request, 'posts.html', {'posts': posts})


@login_required(login_url='/login')
def edit_post(request, pid):
    instance = Posts.objects.get(id=pid)
    if request.method == 'POST':
        form = PostForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts')
    else:
        form = PostForm(instance=instance)
        return render(request, 'edit_post.html', {'form': form})


@login_required(login_url='/login')
def delete_post(request,pid):
    Posts.objects.get(id=pid).delete()
    return redirect('/posts')


@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect('/login')
