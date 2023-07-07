from .models import Authors, Books
from rest_framework import serializers

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields='__all__'
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'