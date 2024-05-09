from django.shortcuts import render, redirect
from .models import Message, Post
from django.http import JsonResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


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
