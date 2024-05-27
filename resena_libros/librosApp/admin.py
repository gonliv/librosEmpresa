from django.contrib import admin
from .models import CustomUser, Author, Genre, Book, Review, Contact


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Contact)