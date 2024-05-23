from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'created_at']
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'parent', 'created_at', 'updated_at', 'replies']

    def get_replies(self, obj):
        if obj.replies:
            return CommentSerializer(obj.replies.all(), many=True).data
        return []