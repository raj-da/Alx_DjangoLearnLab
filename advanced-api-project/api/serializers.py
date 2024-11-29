from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("publication year can not be after current year!")

        return data

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer()
    class Meta:
        model = Author
        fields = ('name')
