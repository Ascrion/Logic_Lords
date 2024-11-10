from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('faq/', views.faq, name='faq'),
    path('login/', views.sign_in, name='login'),  # URL for login view
    path('signup-page/', views.signup, name='signup-page'),
    path('profile/', views.profile, name='profile'),  # Logged-in user's profile
    path('profile/<str:username>/', views.user_profile, name='user_profile'),  # Specific user profile
]
