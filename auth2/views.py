from .models import Book

from rest_framework import viewsets, pagination
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from django.utils import dateparse

# from .models import Something
from .serializers import BookSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class VerifyAPIView(APIView):

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get(self, request):
        queryset = self.queryset.filter(id=self.request.user.id)
        if (queryset):
            resp = {
                'valid': True,
                'id': queryset[0].id,
                'email': queryset[0].email
            }

        return Response(resp)
      
from rest_framework import viewsets, pagination

from rest_framework import pagination

class CustomPagination(pagination.BasePagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'total_count': self.page.paginator.count,
            'previous_link': self.get_previous_link(),
            'next_link': self.get_next_link()
        })


class BookAPIView(APIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


    def get(self, request):
        title = request.GET.get('title',None)
        author = request.GET.get('author', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        page = request.GET.get('page', None)
        per_page = request.GET.get('per_page', None)


        q = Q()
        if title:
            q = q & Q(title=title)
        if author:
            q = q & Q(author=author)
        
        if start_date and end_date:
            q = q & (Q(published_date__gte=start_date) & Q(published_date__lte=end_date))
        elif start_date:
            q = q & Q(published_date__gte=start_date)
        
        books = Book.objects.filter(user=self.request.user.id)
        books = books.filter(q)
        data = BookSerializer(books, many=True).data
        return Response(data)

    def post(self, request):
        book = Book.objects.create(
            title=request.data['title'],
            author=request.data['author'],
            isbn=request.data['isbn'],
            published_date=request.data['published_date'],
            user=request.user,
        )
        book.save()
        data = BookSerializer(book).data

        return Response(data)





    


    



