from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Book, Something
from .serializers import BookResponseSerializer, BookSerializer, SomethingSerializer, SomethingElseSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

    def get_queryset(self):  
        queryset = super().get_queryset().filter(user=self.request.user)

        paginator = Paginator(queryset, per_page=2)
        page = paginator.page(2).object_list
        print('page ', page)
        return queryset




class BookAPIView(APIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        title = request.GET.get('title',None)
        author = request.GET.get('author', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        page_no = int(request.GET.get('page', '1'))
        per_page = int(request.GET.get('per_page', '2'))
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
        print(books)
        data = BookResponseSerializer(books, many=True).data
        paginator = Paginator(books, per_page=per_page)
        if page_no > paginator.num_pages:
            page_no = paginator.num_pages
        page = paginator.page(page_no).object_list
        data = BookResponseSerializer(page, many=True).data
        response = {
            "total": paginator.count,
            "page": page_no,
            "per_page": per_page,
            "books": data
        }
        return Response(response)

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


class SomethingElse(generics.CreateAPIView):
    serializer_class = SomethingElseSerializer
    queryset = Something.objects.all()


class SomethingViewSet(viewsets.ModelViewSet):

    serializer_class = SomethingSerializer
    queryset = Something.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):  
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
    
    def create(self, request):
        print(request.data)
        thing = Something.objects.create(
            user=request.user,
            name=request.data['name']
        )
        serializer = SomethingSerializer(thing).data
        return Response(serializer)

    # def partial_update(self, request, pk=None):
    #     print(request.data)
    #     return Response({'message': 'something'})

class SomeAPIView(generics.GenericAPIView):
    serializer_class = SomethingSerializer
    queryset = Something.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('request. ', request.data)
        return Response({'message': 'something'})
    
    def patch(self, request):
        return Response({'':1}) 
    def put(self, request):
        return Response({'':1})
    def delete(self, request):
        return Response({'':1})
    










