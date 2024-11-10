from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserFiles
from .forms import FileUploadForm
import os
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def how_it_works(request):
    return render(request, 'how_it_works.html')

def faq(request):
    return render(request, 'faq.html')

# Login page view (to avoid name conflict with Django's built-in login)
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

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered. Please use a different email.')
            return render(request, 'signup-page.html')

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
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('user_profile', kwargs={'username': user.username}))
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'my-profile-page.html', {'user': request.user})

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_files = UserFiles.objects.filter(user=user)
    return render(request, 'my-profile-page.html', {'user': user, 'user_files': user_files})


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            # Define the output directory path
            output_dir = os.path.join(settings.BASE_DIR, "uploads")

            # Try to create the directory if it doesn't exist
            try:
                os.makedirs(output_dir, exist_ok=True)  # Create the directory
                print("Directory created successfully or already exists.")
            except Exception as e:
                print(f"Failed to create directory: {e}")
                messages.error(request, 'Failed to create upload directory.')
                return render(request, 'upload_file.html', {'form': form})

            # Define the full path for saving the uploaded file
            output_path = os.path.join(output_dir, uploaded_file.name)
            try:
                with open(output_path, "wb") as file:
                    for chunk in uploaded_file.chunks():
                        file.write(chunk)
                print("File uploaded and saved successfully.")
                messages.success(request, 'File uploaded and saved successfully!')
            except Exception as e:
                print(f"Failed to save file: {e}")
                messages.error(request, 'Failed to save uploaded file.')

            return redirect('profile')  # Redirect to profile after upload
        else:
            messages.error(request, 'File upload failed. Please check the form for errors.')
    else:
        form = FileUploadForm()

    return render(request, 'upload_file.html', {'form': form})
