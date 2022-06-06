"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from movies.views import RegistrationView, ProfileCreateView, ProfileUpdateView

urlpatterns = [
    path('accounts/profile/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('accounts/profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('accounts/registration/', RegistrationView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('movies.urls'), name='movies'),
    path('books/', include('books.urls'), name='books'),  #budou obsahovat urls z movies, ktere jsme si vytvorili
]
