from django.urls import path
from .views import list_books, views, register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_View(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]