from django.urls import path, include
from applications.account.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('activate/', ActivationView )


urlpatterns = [
path('register/' , RegisterAPIVew.as_view()),
path('activate/<uuid:activation_code>/' , ActivationView.as_view()),
# path('activate/<uuid:activation_code>/', include(router.urls)),
path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]