from sys import path_hooks

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import BookViewSet, BookCategoryViewSet, BookGeneralViewSet

router = DefaultRouter()
router.register('category', BookCategoryViewSet)
router.register('book', BookViewSet)
router.register('genre', BookGeneralViewSet)

urlpatterns = [
    path('', include(router.urls))
]