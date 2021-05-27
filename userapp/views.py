from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from . serializers import userregserializer,userloginserializer
from.models import User
from rest_framework_jwt.settings import api_settings


#JWT_PAYLOAD_HANDLER= api_settings.JWT_PAYLOAD_HANDLER
#JWT_ENCODE_HANDLER=   api_settings.JWT_ENCODE_HANDLER

# USER Registration Code--------------------------------------------------------------------------->

class userregview(CreateAPIView):
    serializer_class = userregserializer
    permission_classes = (AllowAny,)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        #user=User.objects.create_user(email=request.data.get("email"),password=request.data.get("password"))
        #print("jdsfjkf",user.id)
        #payload = JWT_PAYLOAD_HANDLER(user)  # the data we want to pass as payload.
        #jwt_token = JWT_ENCODE_HANDLER(payload)
        #serializer.is_valid(raise_exception=True)
        #serializer.data['token']=jwt_token
        #serializer=self.serializer_class(data=serializer.data)

        #serializer.is_valid(raise_exception=True)

        serializer.save()
        #print(serializer.data['token'])

        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': "User Registered Succesfully",
            #'token': jwt_token,
            #'id': user.id,
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)



# Login Code--------------------------------------------------------------

class userlogin(GenericAPIView):
    serializer_class = userloginserializer
    permission_classes = (AllowAny,)

    def post(self,request):
        queryset = User.objects.all()
        serializer = userloginserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=get_object_or_404(queryset,email=request.data.get("email"))
        #print("djn",user,user.name)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': "User Logged in Succesfully",
            'token': serializer.data['token'],
            'id':user.id,

        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


