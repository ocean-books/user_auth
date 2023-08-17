# Django
from django.urls import path

# Project
from apps.user.api import CustomUserAuthAPIView, OTPVerifyAPIView

urlpatterns = [
    path('auth/', CustomUserAuthAPIView.as_view(), name='user_auth'),
    path('verify/<str:phone_number>/', OTPVerifyAPIView.as_view(), name='verify_code'),
]
