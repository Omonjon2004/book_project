from django.urls import path

from account.auth.login import LoginView
from account.auth.register import RegistrationView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegistrationView.as_view()),
]