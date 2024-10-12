from rest_framework.generics import CreateAPIView

from account.auth.login.serializers import LoginSerializer
from account.models import Account


class LoginView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = LoginSerializer


__all__ = ['LoginView']