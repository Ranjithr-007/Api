from django.shortcuts import render
from .serializers import UserRegister
from rest_framework.views import APIView
from django.contrib.auth.models import User, auth
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
from . models import *
from rest_framework import viewsets
from .serializers import BookingSerializer
from rest_framework import status 
import datetime
# Create your views here.



#User Registration
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

#Login
class welcome(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'user':str(request.user), 'userid':str(request.user.id)}
        return Response(content)




dict = {"2021-11-28 10:00","2021-11-28 10:30","2021-11-28 11:00","2021-11-28 11:30","2021-11-28 12:00","2021-11-28 12:30","2021-11-28 1:00","2021-11-28 1:30","2021-11-28 2:00","2021-11-28 2:30","2021-11-28 3:00","2021-11-28 3:30","2021-11-28 4:00","2021-11-28 4:30","2021-11-28 5:00"}



response = {}



class Book_slot(APIView):
    

    #Function for Show Teacher Availabilty
    def get(self, request):

        permission_classes = (IsAuthenticated,)
        flag = True
        for item in dict:
            booking = Booking.objects.filter(time_slot=item)
            if booking ==  3 :
                flag = False

        response = {'item':flag }
        return Response (data=response, status=status.HTTP_200_OK)
    
    #Fuction for create slot
    def post(self, request):
        permission_classes = (IsAuthenticated,)

        time_slot = request.data(time_slot)
        booking = Booking.objects.filter(time_slot=request.time_slot)

        if booking == 2 :
            booking = Booking.objects.create(user=request.user, time_slot=request.data.time_slot)
        else:
            response = {
            'status': 'request was submitted'
            }
        return Response(response)

            
            

           
