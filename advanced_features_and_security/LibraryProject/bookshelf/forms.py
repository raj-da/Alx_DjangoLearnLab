# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    """Form for searching books with validation."""
    book_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'}),
    )

class BookForm(forms.ModelForm):
    """Form for creating or updating a book."""
    class Meta:
        model = Book
        fields = ['name', 'author', 'published_date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Book Name'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author Name'}),
        }

    def clean_name(self):
        """Validate and sanitize book name input."""
        name = self.cleaned_data.get('name')
        if any(char in name for char in ['<', '>', '{', '}']):
            raise forms.ValidationError("Invalid characters in book name.")
        return name
