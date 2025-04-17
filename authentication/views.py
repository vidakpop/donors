from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class SignUpView(APIView):
    permission_classes= [AllowAny]

    def post(self, request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user=User.objects.create_user(username=username, email=email, password=password)
        refresh=RefreshToken.for_user(user)

        return Response({
            "username": user.username,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
