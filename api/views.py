from django.shortcuts import render
from .serializers import LoginSerializer
from app.models import Login
from rest_framework import status, generics, mixins, viewsets

# Create your views here.


class LCAPIView(generics.ListCreateAPIView):
	serializer_class = LoginSerializer
	queryset = Login.objects.all()


class RUDAPIView(generics.ListCreateAPIView):
	serializer_class = LoginSerializer
	queryset = Login.objects.all()

