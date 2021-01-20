"""Define padrões de URL para users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Página para login e logoff.
    path('', include('django.contrib.auth.urls')),

    # Página para registrar.
    path('register/', views.register, name='register'),
]
