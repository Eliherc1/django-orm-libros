from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors contiene los autores de cada libro
    def __repr__(self):
        return f" {self.title} "
    def __str__(self):
        return f" {self.title}  "

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books =   models.ManyToManyField(Book, related_name='authors')
    notas = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __repr__(self):
        return f" {self.first_name} {self.last_name} "
    def __str__(self):
        return f" {self.first_name} {self.last_name} "
