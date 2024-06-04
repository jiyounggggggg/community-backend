from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment, Board
from .serializers import BoardPostsSerializer, PostSerializer, CommentSerializer, BoardSerializer
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response


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
    
    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        if post_id:
            return self.queryset.filter(post_id=post_id, parent__isnull=True)
        return self.queryset.none()
    
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_serializer_class(self):
        if self.action == 'with_posts':
            return BoardPostsSerializer
        return BoardSerializer

    @action(detail=True, methods=['get'], url_path='with-posts')
    def with_posts(self, request, pk=None):
        board = self.get_object()
        serializer = self.get_serializer(board)
        return Response({
            'board': {
                'id': serializer.data['id'],
                'name': serializer.data['name'],
                'description': serializer.data['description'],
                'created_at': serializer.data['created_at'],
                'updated_at': serializer.data['updated_at'],
                'created_by': serializer.data['created_by']
            },
            'posts': serializer.data['posts'],
        })    
