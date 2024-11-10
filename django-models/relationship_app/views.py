from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request,"relationship_app/list_books.html",context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Library = self.get_object()
        context['books'] = Library.books.all()
        return context
    

# Registration view
def register(request):
    if request.method == "post":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'