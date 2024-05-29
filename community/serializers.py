from rest_framework import serializers
from .models import Post, Comment, Board

class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        extra_fields = ['comment_count']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'