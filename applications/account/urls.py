from django.urls import path, include
from applications.account.views import *
from django.urls import path
from . import views
# from models import ChangePassword
from .views import ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('activate/', ActivationView )


    

urlpatterns = [
path('register/' , RegisterAPIVew.as_view()),
path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
path('activate/<uuid:activation_code>/' , ActivationView.as_view()),
path('change-password/', ChangePasswordView.as_view(), name='change-password'),
path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('logout/',LogoutAPIView.as_view()),
path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




