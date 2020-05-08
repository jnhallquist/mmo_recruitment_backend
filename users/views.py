from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
