from django.urls import path, include
from . import views
from applications.account.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



    

urlpatterns = [
path('register/' , RegisterAPIVew.as_view()),
path('activate/<uuid:activation_code>/' , ActivationView.as_view()),
path('change_password/', ChangePasswordView.as_view(), name='change_password'),
path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('logout/',LogoutAPIView.as_view()),
path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('reset_password/',ResetPasswordView.as_view()),
path('confirm/',ConfirmPasswordView.as_view()),

]

