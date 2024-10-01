from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from .models import Book

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['username'],
            last_name=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(write_only=False, required=True)
    # author = serializers.CharField(write_only=False, required=True)
    # isbn = serializers.CharField(write_only=False, required=True)
    # published_date = serializers.CharField(write_only=False, required=True)
    # user = serializers.CharField(write_only=False, required=True)

    class Meta:
        model = Book
        fields = '__all__'
    
    # def create(self, validated_data):
    #     book = Book.objects.create(
    #         title=validated_data['title'],
    #         author=validated_data['author'],
    #         isbn=validated_data['isbn'],
    #         published_date=validated_data['published_date']
    #     )


    #     book.save()

    #     return book
