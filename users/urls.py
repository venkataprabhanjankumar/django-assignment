from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_url, name='default_url'),
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.user_logout, name='logout'),
    path('newpost', views.new_post, name='new_post'),
    path('posts', views.user_posts, name='userposts'),
    path('post/edit/<int:pid>', views.edit_post),
    path('post/delete/<int:pid>', views.delete_post)
]
