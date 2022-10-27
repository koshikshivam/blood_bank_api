from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import views
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User    
from rest_framework.permissions import BasePermission 
from rest_framework.authentication import BasicAuthentication, BaseAuthentication,SessionAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.




class BloodChoiceModelViewSet(viewsets.ModelViewSet):
    queryset = Blood_choice.objects.all()
    serializer_class=BloodChoiceSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

class CatagoryModelViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=UserProfileSerializer
    
    
class UserProfileModelViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
class BloodDonationModelViewset(viewsets.ModelViewSet):
    queryset = Blood_Donation.objects.all()
    serializer_class = BloodDonationSerializer
    
    
class OrderModelViewsets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    

    
    

    
    