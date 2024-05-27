from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactFormForm, CustomUserCreationForm, ReviewForm, BookForm
from django.contrib.auth.decorators import login_required
from .models import ContactForm, Book, Review, Author, Genre
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'index.html')

def welcome(request):
    return render(request, 'welcome.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(** form.cleaned_data)
            return HttpResponseRedirect('/success')
        else: 
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html', {})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'welcome')
            return redirect(next_url)
        else:
            messages.error(request, 'Su nombre de usuario y contraseña no coinciden. Inténtalo de nuevo.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)  # Autenticar al usuario
            if user is not None:
                login(request, user)  # Iniciar sesión
                return redirect('index')  # Redirigir al usuario a la página de inicio después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')

@login_required
def profile_view(request):
    user_type = request.user.user_type
    return render(request, 'profile.html', {'user_type': user_type})

def library_view(request):
    # Obtener todos los libros
    all_books = Book.objects.all()
    
    # Filtros por género y autor
    genre_id = request.GET.get('genre')
    if genre_id:
        all_books = all_books.filter(genres__id=genre_id)
    
    author_id = request.GET.get('author')
    if author_id:
        all_books = all_books.filter(author__id=author_id)
    
    # Número de libros por página
    books_per_page = 8
    
    # Obtener el número de página actual
    page_number = request.GET.get('page', 1)
    
    # Crear un objeto Paginator
    paginator = Paginator(all_books, books_per_page)
    
    # Obtener los libros para la página actual
    current_page_books = paginator.get_page(page_number)
    
    # Calcular si hay una página anterior y siguiente
    has_previous_page = current_page_books.has_previous()
    has_next_page = current_page_books.has_next()
    
    context = {
        'books': current_page_books,
        'genres': Genre.objects.all(),  # Pasar todos los géneros a la plantilla
        'authors': Author.objects.all(),  # Pasar todos los autores a la plantilla
        'has_previous_page': has_previous_page,
        'has_next_page': has_next_page,
        'previous_page_number': current_page_books.previous_page_number() if has_previous_page else None,
        'next_page_number': current_page_books.next_page_number() if has_next_page else None,
    }
    
    return render(request, 'library.html', context)

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    review = Review.objects.filter(user=request.user, book=book).first()
    reviews = book.reviews.all()

    if request.method == 'POST':
        if review:
            form = ReviewForm(request.POST, instance=review)
        else:
            form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book_detail', pk=pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'form': form})

def is_admin(user):
    return user.is_authenticated and user.user_type == 'admin'

@login_required
def book_creation_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library')
    else:
        form = BookForm()

    authors = Author.objects.all()
    genres = Genre.objects.all()
    return render(request, 'book_creation.html', {'form': form, 'authors': authors, 'genres': genres})