from django.shortcuts import render
from .serializers import UserRegister
from rest_framework.views import APIView
from django.contrib.auth.models import User, auth
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
from . models import Teacher
from rest_framework import viewsets
from .serializers import TeacherSerializer

import datetime
# Create your views here.
dict = {'10.00','10.30',"11.00","11.30","12.00","12.30","1.00","1.30","2.00","2.30","3.00","3.30","4.00","4.30","5.00"}


class register(APIView):

    def post(self,request,format=None):
        serializer = UserRegister(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response']='registered!!!'
            data['username']= account.username
            data['email']=account.email
            token.create=Token.objects.get_or_create(user=account)
            data['token'] = token.key
        else:
            data= serializer.errors
        return Response(data)


class welcome(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'user':str(request.user), 'userid':str(request.user.id)}
        return Response(content)


class teacher(APIView):
   
    def get(self, request):
        user = User.objects.all()
        teacher = Teacher.objects.filter(data=timestamp)
        if dict == 3:
           print(True)
        elif dict == 2 :
            print(False)
        serializer = TeacherSerializer(user)
        return Response(serilizer.data)

