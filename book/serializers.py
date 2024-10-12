from rest_framework.serializers import ModelSerializer

from book.models import BookCategory, Book, BookGenre


class BookCategorySerializer(ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ("id", "name")


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "summary", "cover", "category")

class BookGenreSerializer(ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ("id", "name")

