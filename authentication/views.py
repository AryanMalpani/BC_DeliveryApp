from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication import serializers
import authentication
from authentication.serializers import LoginSerializer, RegisterSerialzier
from rest_framework import response, status
from django.contrib.auth import authenticate
# Create your views here.


class AuthUserAPIView(GenericAPIView):
    
    def get(self, request):
        user = request.user
        serializer = RegisterSerialzier(user)
        return response.Response({'user':serializer.data})

class RegisterAPIView(GenericAPIView):

    authentication_classes = []

    serializer_class = RegisterSerialzier

    def post(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return response.Response(serializer.data, status = status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):

    authentication_classes = [] #this is to avoid using settings waala auth

    serializer_class = LoginSerializer

    def post(self,request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username = email, password = password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status = status.HTTP_200_OK)
        
        return response.Response({'message': "Invalid Credentials, Try Again"}, status = status.HTTP_401_UNAUTHORIZED)