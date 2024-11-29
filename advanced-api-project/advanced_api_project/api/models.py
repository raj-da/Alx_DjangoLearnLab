from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=20)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=None, related_name='books')
