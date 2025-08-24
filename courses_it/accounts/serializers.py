from rest_framework import serializers
from .models import CustomUser
 
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        
    def validation_email(self, value):
        # Validate email format
        validator = EmailValidator()
        try:
            validator(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format")
        # Check email uniqueness
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use")
        return value
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        # token['user_id'] = user.id
        # token['email'] = user.email
        return token