from django.contrib import admin
from .models import ContactForm, CustomUser, Author, Genre, Book, Review, ContactForm


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(ContactForm)