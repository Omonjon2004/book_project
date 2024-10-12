from rest_framework.generics import CreateAPIView

from account.auth.register.serializers import RegistrationSerializer
from account.models import Account


class RegistrationView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegistrationSerializer

__all__ = ['RegistrationView']