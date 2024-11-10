from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('faq/', views.faq, name='faq'),
    path('login/', views.sign_in, name='login'),  # URL for login view
    path('signup-page/', views.signup, name='signup-page'),
    path('my-profile/', views.profile, name='profile'),  # Logged-in user's profile
    path('profile/<str:username>/', views.user_profile, name='user_profile'),  # Specific user profile
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)