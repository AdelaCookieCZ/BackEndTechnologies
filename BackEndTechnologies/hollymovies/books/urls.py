from django.urls import path

from books.views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]

