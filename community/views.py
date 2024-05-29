from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment, Board
from .serializers import PostSerializer, CommentSerializer, BoardSerializer
from django.db.models import Count

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        queryset = Post.objects.all()
        board_id = self.request.query_params.get('boardId', None)
        if board_id is not None:
            queryset = queryset.filter(board_id=board_id)
            
        # 댓글 수를 주석으로 추가
        queryset = queryset.annotate(comment_count=Count('comments'))
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer    
