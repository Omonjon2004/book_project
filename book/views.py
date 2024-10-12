from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from book.models import BookCategory, Book, BookGenre
from book.serializers import BookCategorySerializer, BookSerializer, BookGenreSerializer


class BookCategoryViewSet(ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookGeneralViewSet(ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    
