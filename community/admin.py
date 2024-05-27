from django.contrib import admin
from .models import Board, Post, Comment, Like, Banner, SeoTag

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'created_by']
    search_fields = ['name', 'description']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'board', 'created_at', 'created_by', 'views']
    search_fields = ['title', 'content']
    list_filter = ['board', 'created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'post', 'parent', 'created_at', 'created_by']
    search_fields = ['content']
    list_filter = ['post', 'created_at']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'object_id', 'created_at']
    search_fields = ['user__username']
    list_filter = ['content_type', 'created_at']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'board', 'created_at']
    search_fields = ['title']
    list_filter = ['board', 'created_at']

@admin.register(SeoTag)
class SeoTagAdmin(admin.ModelAdmin):
    list_display = ['url', 'title', 'created_at', 'updated_at']
    search_fields = ['url', 'title', 'meta_description', 'meta_keywords', 'meta_author']
    list_filter = ['created_at', 'updated_at']