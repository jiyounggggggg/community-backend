"""
URL configuration for community_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users.views import CustomTokenObtainPairView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("community.urls")),
    path("api/users/", include("users.urls")),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # todo delete this
    # path("api/messages/", message_list, name="message_list"),
    # path("api/post/", create_post, name="create_post"),
    # path("api/board/list/", post_list, name="post_list"),
    # path("apiold/", include(router.urls)),
]
