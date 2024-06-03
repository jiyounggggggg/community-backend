from rest_framework import serializers
from .models import Post, Comment, Board

class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True)
    board_name = serializers.CharField(source='board.name', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'created_by', 'views', 'comment_count', 'board_name', 'board']
        extra_fields = ['comment_count']

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['id', 'post', 'parent', 'content', 'created_at', 'updated_at', 'created_by', 'replies']
    
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'