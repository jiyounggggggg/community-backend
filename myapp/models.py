from django.conf import settings
from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.text
    

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")  # 게시글 제목
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자")  # 게시글 작성자
    author = models.CharField(max_length=200, verbose_name="작성자")  # 게시글 작성자
    content = models.TextField(verbose_name="글내용")  # 게시글 내용
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")  # 게시글 작성 시간 (자동으로 현재 시간 저장)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]