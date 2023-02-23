from rest_framework import serializers
from django.contrib.auth import get_user_model , authenticate
from applications.account.send_email import *
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')


    def validate_email(self, email):
        return email

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Введенные пароли не совподают!!!')
        return attrs

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)

        return user

 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True) 
    password = serializers.CharField(required=True)

    def validate_email(self,email):
        if User.objects.filter(email=email).exists():
            return email
        raise serializers.ValidationError('Пользователь не найден!')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError('Неверный пароль!')
        attrs['user'] = user    
        return attrs



class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validate_email(self,email):
        if User.objects.filter(email=email).exists():
            return email
        raise serializers.ValidationError('Пользователь не найден!')
        



class ConfirmPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True, min_length=6, write_only=True)
    activation_code = serializers.CharField(required=True, write_only=True)

    def validate_email(self,email):
        if User.objects.filter(email=email).exists():
            return email
        raise serializers.ValidationError('Такого пользователя не существует!')
    
    def validate(self, attrs):

        p1 = attrs.get('new_password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Введенные пароли не совподают!!!')
        
        activation_code = attrs.pop('activation_code')
        user = get_object_or_404(get_user_model(), email=attrs['email'])
        
        if not hasattr(user, 'activation_code') or user.activation_code != activation_code:
            raise serializers.ValidationError('Неверный код активации!')
        
        attrs['user'] = user
        return attrs
