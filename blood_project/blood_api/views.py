from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import views
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
# Create your views here.




class BloodChoiceModelViewSet(viewsets.ModelViewSet):
    queryset = Blood_choice.objects.all()
    serializer_class=BloodChoiceSerializer
    

class CatagoryModelViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=UserProfileSerializer
    
    
class UserProfileModelViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class BloodDonationModelViewset(viewsets.ModelViewSet):
    queryset = Blood_Donation.objects.all()
    serializer_class = BloodDonationSerializer
    
    
class OrderModelViewsets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    

    
    

    
    