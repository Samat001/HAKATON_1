from rest_framework.views import APIView
from applications.account.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import *
from datetime import datetime
from django.shortcuts import get_object_or_404
from .serializers import ConfirmPasswordSerializer


User = get_user_model()
class RegisterAPIVew(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        

        return Response('Вы успешно зарегистрировались , Вам отправлено письмо с активацией ', status=201) 


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'Сообщение': 'Успешно активировались'}, status=200)
        except User.DoesNotExist:
            return Response({'Сообщение': 'Активационный код устарел'}, status=400)


class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            token = Token.objects.get(user=user).delete()
            return Response('Вы успешно разлогинились', status=200)
        except:
            return Response(status=403)




class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Не правильный пароль"]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'Успешно',
                'code': status.HTTP_200_OK,
                'message': 'Пароль успешно сменен',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            user.create_activation_code()
            user.save()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',user.activation_code)
            send_resset_code(user.email, user.activation_code)
            
            
            return Response({'message': 'Запрос на смену пароля успешно отправлен'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ConfirmPasswordView(APIView):
    def post(self, request):
        serializer = ConfirmPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            new_password = serializer.validated_data['new_password']
            user.set_password(new_password)
            if hasattr(user, 'activation_code'):
                user.activation_code = ''
            user.save()
            return Response({'message': 'Пароль успешно изменен'})
        return Response(serializer.errors, status=400)


    
    