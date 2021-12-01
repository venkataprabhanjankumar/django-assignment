from django.contrib import admin
from .models import UserModel, Posts

admin.site.register(UserModel)
admin.site.register(Posts)
