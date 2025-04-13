from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegistrationForm, LoginForm, ContactForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def about_me(request):
    return render(request, 'about_me.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Error creating account.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, 'Logged in successfully!')

        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def thank_you_view(request):
    return render(request, 'thank_you.html')
