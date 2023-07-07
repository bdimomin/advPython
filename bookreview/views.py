from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class AuthorView(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    # permission_classes = [permissions.IsAuthenticated]

class BookView(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    # permission_classes = [permissions.IsAuthenticated]