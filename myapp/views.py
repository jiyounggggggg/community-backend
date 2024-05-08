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
        title = request.POST.get('title')
        # author = request.user  # 현재 로그인한 사용자
        author = 'Anonymous'
        content = request.POST.get('content')
        created_at = timezone.now()

        # Post 모델에 데이터 저장
        print('111:', title, author, content, created_at)
        post = Post(title=title, author=author, content=content, created_at=created_at)
        post.save()

        # return redirect('post_list')  # 저장 후 리스트 페이지로 리디렉션 (URL 이름은 상황에 맞게 변경)
    # return render(request, 'create_post.html')
