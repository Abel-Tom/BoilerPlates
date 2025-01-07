
from django.urls import path, include
from .views import SomethingViewSet, SomethingElse, SomeAPIView, BookAPIView, MyModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'things', SomethingViewSet, basename='thing')
router.register(r'books', MyModelViewSet, basename='books')

urlpatterns = [
    path('else/', SomethingElse.as_view(), name='else'),
    path('some/', SomeAPIView.as_view(), name='some'),
    path('api/books/', BookAPIView.as_view(), name='books'),
    path('', include(router.urls)),
]

