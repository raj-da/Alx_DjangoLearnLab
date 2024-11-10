from django.urls import path
from .views import list_books, views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk', views.LibraryDetailView.as_view(), name='library_detail')
]