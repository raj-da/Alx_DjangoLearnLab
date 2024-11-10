from django.shortcuts import render
from django.views.generic.detail import DetailView
from models import Library, Book

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