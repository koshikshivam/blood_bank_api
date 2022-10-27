from rest_framework import serializers
from .models import *



class BloodChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood_choice
        fields = "__all__"

class  CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        


class BloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood_Donation
        fields = "__all__"
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        