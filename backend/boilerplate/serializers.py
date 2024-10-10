from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Something
from django.contrib.auth.password_validation import validate_password

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
class SomethingSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = Something
        fields = ['id', 'name', 'user', 'user_name']
    
    def get_user_name(self, instance):
        return instance.user.username
    
class SomethingElseSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = Something
        fields = ['id', 'name', 'user', 'user_name']
    
    def get_user_name(self, instance):
        return instance.user.username

class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(write_only=False, required=True)
    # author = serializers.CharField(write_only=False, required=True)
    # isbn = serializers.CharField(write_only=False, required=True)
    # published_date = serializers.CharField(write_only=False, required=True)
    # user = serializers.CharField(write_only=False, required=True)

    class Meta:
        model = Book
        fields = '__all__'
    
class BookResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['user']
    

        