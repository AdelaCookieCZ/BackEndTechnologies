from django.urls import path

from books.views import BookListView, BookDetailView, BookUpdateView, AuthorListView, \
    AuthorUpdateView, AuthorDetailView, DeleteBookView, DeleteAuthorView, CreateAuthorView, CreateBookView


urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('author/update/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('author/create/', CreateAuthorView.as_view(), name='author_create'),
    path('book/create/', CreateBookView.as_view(), name='book_create'),
    path('book/delete/<int:pk>', DeleteBookView.as_view(), name='book_delete'),
    path('author/delete/<int:pk>', DeleteAuthorView.as_view(), name='author_delete'),
]

