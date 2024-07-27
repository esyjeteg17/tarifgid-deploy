from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Tariff, Region
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


""" class UpdateFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['isFavorite']


    def update(self, instance, validated_data):
        instance.isFavorite = validated_data.get('isFavorite', instance.isFavorite)
        instance.save()
        return instance """
    

""" class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("Validated Data:", validated_data)
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    def validate(self, data):
        print("Data to validate:", data)
        if not data.get('email'):
            raise serializers.ValidationError('Email is required')
        if not data.get('username'):
            raise serializers.ValidationError('Username is required')
        if not data.get('password'):
            raise serializers.ValidationError('Password is required')
        return data

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        if not all(credentials.values()):
            raise serializers.ValidationError('Email and password are required')

        print("Credentials for validation:", credentials)

        try:
            user = User.objects.get(email=credentials['email'])
            print(f"User found: {user.email}")
        except User.DoesNotExist:
            print("User with this email does not exist")
            raise AuthenticationFailed('User with this email does not exist')

        if not user.check_password(credentials['password']):
            print("Incorrect password")
            raise AuthenticationFailed('Incorrect password')

        data = super().validate(attrs)
        data['user'] = UserSerializer(user).data

        print("Token validation success:", data)

        return data """
    
""" 


class ModemTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModemTariff
        fields = '__all__'


class HomephoneTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomephoneTariff
        fields = '__all__'


class TVTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVTariff
        fields = '__all__'



class InternetTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternetTariff
        fields = '__all__'



class SmartTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartTariff
        fields = '__all__'



 """


