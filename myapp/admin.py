from django.contrib import admin
from .models import Message, Post, Comment

# Register your models here.
models = [Message, Post, Comment]

for model in models:
    admin.site.register(model)