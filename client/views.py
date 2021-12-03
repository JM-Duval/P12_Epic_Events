from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from client.serializers import UserSerializer, RegisterSerializer, ClientSerializer
from client.models import Client


class ClientViewset(viewsets.ModelViewSet):

    serializer_class = ClientSerializer

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name')
        email = self.request.query_params.get('email')
        if first_name is not None:
            return Client.objects.filter(first_name=first_name)
        elif email is not None:
            return Client.objects.filter(email=email)
        else:
            return Client.objects.all()


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )