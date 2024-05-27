from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactFormForm, CustomUserCreationForm
from .models import ContactForm


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