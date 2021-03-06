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




dict = {"2021-11-29 10:00","2021-11-29 10:30","2021-11-29 11:00","2021-11-29 11:30","2021-11-29 12:00","2021-11-29 12:30","2021-11-29 1:00","2021-11-29 1:30","2021-11-29 2:00","2021-11-29 2:30","2021-11-29 3:00","2021-11-29 3:30","2021-11-29 4:00","2021-11-29 4:30","2021-11-29 5:00"}



response = {}



class Book_slot(APIView):
    permission_classes = (IsAuthenticated,)

    #Function for Show Teacher Availabilty
    def get(self, request):

        
        flag = True
        for item in dict:
            booking = Booking.objects.filter(time_slot=item)
            if booking ==  3 :  #check available teacher > 2
                flag = False

        response = {item, flag}

        return Response (data=response, status=status.HTTP_200_OK)
    
    #Fuction for find  Student Booking 
    def post(self, request):

        time_slot=request.data()
        booking = Booking.objects.filter(time_slot)
                                     
        if booking == 2 : #we can check teacher <2
            booking = Booking.objects.create(user=request.user, time_slot=request.data.time_slot) #Create booking Return student id
        else:
            response = {
            'status': 'request was submitted'
            }
        return Response(response)

            
            

           
