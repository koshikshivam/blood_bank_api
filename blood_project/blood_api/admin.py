from django.contrib import admin
# Register your models here.
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Blood_Donation)
admin.site.register(Order)
