import PyPDF2
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserFiles
from .forms import FileUploadForm

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

@login_required
def user_profile(request, username):
    # Get the user and their files
    user = get_object_or_404(User, username=username)
    user_files = UserFiles.objects.filter(user=user)  # Get files related to the user
    return render(request, 'my-profile-page.html', {'user': user, 'user_files': user_files})

def extract_text_from_pdf(pdf_file):
    """Extracts text from PDF and returns it as a single string."""
    extracted_text = ""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"  # Add newline between pages
        return extracted_text
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
        return None

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded PDF file
            pdf_file = request.FILES['file']
            extracted_text = extract_text_from_pdf(pdf_file)  # Extract text from the PDF

            if extracted_text:
                # Save the extracted text and file name to the database
                user_file = UserFiles(
                    user=request.user,
                    name=form.cleaned_data['name'],
                    file_content=extracted_text
                )
                user_file.save()
                messages.success(request, 'PDF uploaded and processed successfully!')
            else:
                messages.error(request, 'Failed to extract text from PDF.')
            return redirect('profile')
        else:
            messages.error(request, 'File upload failed. Please check the form for errors.')
    else:
        form = FileUploadForm()
    
    return render(request, 'upload_file.html', {'form': form})
