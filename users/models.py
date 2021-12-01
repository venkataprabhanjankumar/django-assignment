from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'


class Posts(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'Posts'
