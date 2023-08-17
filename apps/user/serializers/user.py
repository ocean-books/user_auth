# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import CustomUser


class CustomUserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'phone_number'
        ]


class OTPVerifySerializer(serializers.Serializer):
    otp_code = serializers.CharField(max_length=4)
