
from django.urls import path, include
from auth2.views import  RegisterView, VerifyAPIView,BookAPIView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



router = DefaultRouter()


urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/signup', RegisterView.as_view(), name='auth_register'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/verify/', VerifyAPIView.as_view(), name='verify'),
    path('books/', BookAPIView.as_view(), name='book'),
    # path('books/', BookAPIView, name='book'),
    path('', include(router.urls)),
]
