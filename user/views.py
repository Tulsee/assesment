from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserSerializer


class UserRegistrationViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
