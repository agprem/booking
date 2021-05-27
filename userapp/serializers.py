from rest_framework import serializers
from userapp.models import User
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login


# USer Registration Serializer Code--------------------------------------------------------------------------
class userregserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name','email','password']
        #extra_kwargs={'password':{'writeonly':'True'}}
# token = serializers.CharField(max_length=255,read_only=True)

    def create(self, validated_data):
        name=validated_data.pop('name')
        user = User.objects.create_user(**validated_data)# for creating user object
        return user



# USer Login Serializer Code----------------------------------------------------------------------------------------------------------

JWT_PAYLOAD_HANDLER= api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER=   api_settings.JWT_ENCODE_HANDLER

class userloginserializer(serializers.Serializer):
    token = serializers.CharField(max_length=255,read_only=True)
    email=serializers.EmailField(max_length=255)
    password=serializers.CharField(max_length=50,write_only=True)
    #class Meta:              ------------------------ this does not work with login part throws error email already exists
        #model=User                                     For login purpose use serializers.Serializer else use ModelSerializer
        #fields=['email','password','token']

    def validate(self, data):
        # print("hello")
        email = data.get("email", None)
        password = data.get("password", None)
        print(email,password)
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("A User with this email and password not found")
        try:
            payload = JWT_PAYLOAD_HANDLER(user)  # the data we want to pass as payload.
            jwt_token = JWT_ENCODE_HANDLER(payload)  # the payload that we want to encode.
            update_last_login(None, user)
        except user.DoesNotExist:
            raise serializers.ValidationError("User with this emailID and Password does not exists")
        return {
            'email': user.email,
            'token': jwt_token
        }




