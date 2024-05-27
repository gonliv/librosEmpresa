import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USER_TYPE_CHOICES = (
        ('admin', 'Administrator'),
        ('reader', 'Reader'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='reader')
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users', 
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )

    def __str__(self):
        return self.email

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    followers = models.ManyToManyField(CustomUser, related_name='followed_authors', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    category = models.CharField(max_length=50)
    publication_year = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title

class Review(models.Model):
    content = models.TextField()
    rating = models.PositiveIntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review by {self.user.email} on {self.book.title}"

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.customer_name} - {self.customer_email}"  