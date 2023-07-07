from django.shortcuts import render
from rest_framework import viewsets
from .models import Authors, Books
from .serializers import AuthorSerializers, BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.

class AuthorView(viewsets.ModelViewSet):
    queryset=Authors.objects.all().order_by('id')
    serializer_class=AuthorSerializers
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True,methods=['GET'])
    def books(self,request,pk=None):
        try:
            author=Authors.objects.get(pk=pk)
            books=Books.objects.filter(author=author)
            books_serializers=BookSerializer(books,many=True,context={'request':request})
            return Response(books_serializers.data)
        except Exception as e:
            return Response({'message':'Author is not found'})


class BookView(viewsets.ModelViewSet):
    queryset=Books.objects.all().order_by('id')
    serializer_class=BookSerializer
    # permission_classes = [permissions.IsAuthenticated]



