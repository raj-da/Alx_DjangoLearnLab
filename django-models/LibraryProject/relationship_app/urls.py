from django.urls import path
from .views import book_list, LibraryDetailView, CustomLoginView, CustomLogoutView, register


urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('library/<int:pk', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]