from django.contrib import admin
from django.urls import path, include
from boilerplate.views import SomethingViewSet, SomethingElse, SomeAPIView, BookAPIView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'things', SomethingViewSet, basename='thing')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('else/', SomethingElse.as_view(), name='else'),
    path('some/', SomeAPIView.as_view(), name='some'),
    path('api/books/', BookAPIView.as_view(), name='books'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
