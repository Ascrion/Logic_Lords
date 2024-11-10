from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def how_it_works(request):
    return render(request, 'how_it_works.html')

def faq(request):
    return render(request, 'faq.html')

# Rename this function to avoid conflict with Django's login
def login_page(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup-page.html')

        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'signup-page.html')

        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered. Please use a different email.')
            return render(request, 'signup-page.html')

        # Create user with email as username
        user = User.objects.create_user(
            username=email,  # Set email as the username
            email=email,
            password=password,
        )
        messages.success(request, 'Sign-up successful!')
        return redirect('login')  # Redirect to login page after signup

    return render(request, 'signup-page.html')

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Authenticate using email as the username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the user-specific profile page
            return redirect(reverse('user_profile', kwargs={'username': user.username}))
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required
def profile(request):
    # Render the profile of the logged-in user
    return render(request, 'my-profile-page.html', {'user': request.user})

def user_profile(request, username):
    # View to display profile based on username
    user = get_object_or_404(User, username=username)
    return render(request, 'my-profile-page.html', {'user': user})
