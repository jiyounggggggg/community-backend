from venv import logger
from django.shortcuts import render, redirect
from .models import Message, Post
from django.http import JsonResponse
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# Create your views here.
def message_list(request):
    messages = Message.objects.all().values("id", "text")
    return JsonResponse(list(messages), safe=False)

@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            print("Validated Data: ", serializer.validated_data)
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errors: ", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def post_list(request):
    posts = Post.objects.all().values("id", "title", "author", "content", "created_at")
    return JsonResponse(list(posts), safe=False)

class PostViewSet(viewsets.ModelViewSet):
    logger.info("PostViewSet")
    queryset = Post.objects.defer('content')
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer