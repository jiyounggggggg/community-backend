from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(CustomUserViewSet, self).get_permissions()
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def get_object(self):
        return self.request.user
    
class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        tokens = response.data

        response.set_cookie(
            key='access',
            value=tokens['access'],
            httponly=True,
            secure=True,  # HTTPS를 통해서만 전송
            samesite='Strict'
        )
        response.set_cookie(
            key='refresh',
            value=tokens['refresh'],
            httponly=True,
            secure=True,  # HTTPS를 통해서만 전송
            samesite='Strict'
        )
        return response
