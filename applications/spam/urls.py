from django.urls import path, include
from .views import ContactAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact',ContactAPIView)



urlpatterns = [

    path('', include(router.urls))

]
