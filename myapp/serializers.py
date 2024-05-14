from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ['id', 'title', 'author', 'content', 'created_at']
=======
        fields = '__all__'
>>>>>>> ee3250d76e55f9d359ce856830a86a59642e020c
