from models import Book, Author, Library, Librarian

book = Book.objects.filter(author='Rajaf')

library = Library.objects.all()

librarian = Librarian.objects.filter(library='ox')