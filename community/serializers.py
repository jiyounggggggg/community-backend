from rest_framework import serializers
from .models import Post, Comment, Board

class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    board_name = serializers.CharField(source='board.name', read_only=True)
    username = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'created_by', 'views', 'comment_count', 'board_name', 'username', 'board']
        extra_fields = ['comment_count']

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['id', 'post', 'parent', 'content', 'created_at', 'updated_at', 'created_by', 'replies', 'username']
    
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'

class BoardPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'created_by', 'posts']
        