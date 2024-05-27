from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactFormForm, CustomUserCreationForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .models import ContactForm, Book, Review


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
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')  # Redirigir al usuario a la página de inicio después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def library_view(request):
    # Obtener todos los libros
    all_books = Book.objects.all()
    
    # Número de libros por página
    books_per_page = 8
    
    # Obtener el número de página actual
    page_number = request.GET.get('page', 1)
    
    # Calcula el indice inicial y final de los libros a mostrar en esta página
    start_index = (int(page_number) - 1) * books_per_page
    end_index = start_index + books_per_page
    
    # Obtener los libros para la pagina actual
    current_page_books = all_books[start_index:end_index]
    
    # Calcular si hay una pagina anterior y siguiente
    has_previous_page = start_index > 0
    has_next_page = end_index < len(all_books)
    
    context = {
        'books': current_page_books,
        'has_previous_page': has_previous_page,
        'has_next_page': has_next_page,
        'previous_page_number': int(page_number) - 1 if has_previous_page else None,
        'next_page_number': int(page_number) + 1 if has_next_page else None,
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