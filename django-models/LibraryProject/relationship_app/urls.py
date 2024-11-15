from django.urls import path
from .views import list_books, views


urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete/<int:pk>/', views.delete_book, name='delete-book'), 
]