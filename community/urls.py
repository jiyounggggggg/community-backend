from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, BoardViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet)
router.register(r'boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
