# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root route
    path('index.html', views.index, name='index'),  # Additional route if needed
    path('my-profile-page', views.my_profile_page, name='my_profile_page'),
    path('signin-page', views.signin_page, name='signin_page'),
    path('faq', views.faq, name='faq'),
]
