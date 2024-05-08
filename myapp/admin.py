from django.contrib import admin
from .models import Message, Post

# Register your models here.
models = [Message, Post]

for model in models:
    admin.site.register(model)