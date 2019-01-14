from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView,CreateAPIView
from .models import Test,Photo,User
from .serializers import TestSerializer, PhotoSerializer, UserSerializer
from rest_framework.response import Response

class TestListView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetailView(RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class PhotoListView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoCreateView(CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class LoginView():
    pass

@api_view(['POST'])
def RegView(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        user = User.objects.create(
            useremail = serialized.init_data['email'],
            username = serialized.init_data['username'],
            userpass = serialized.init_data['password']
        )
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)