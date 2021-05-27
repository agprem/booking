from rest_framework import serializers
from .models import advisor

# For Showing all advisor details---------------------------------------------

class advisorviewserializer(serializers.ModelSerializer):
    class Meta:
        model=advisor
        fields=['id','first_name','profilepic','bookingtime','bookingid']



# For Registraion of Advisor----------------------------------------------------------------------------
class advisorregserializer(serializers.ModelSerializer):
    class Meta:
        model=advisor
        fields=['first_name','profilepic']


# For booking advisor---------------------------------------------------------------------------------------------
class advisorbookserializer(serializers.ModelSerializer):
    class Meta:
        model=advisor
        fields=['bookingtime'] # code required to set in prerequest scripts in POSTMAN for taking current time in datetime Format



