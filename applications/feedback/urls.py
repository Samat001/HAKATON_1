from django.urls import path , include
from rest_framework import routers

from .views import LikeViewSet, RatingViewSet, FavoriteViewSet

router = routers.DefaultRouter()
router.register(r'likes', LikeViewSet, basename='likes')
router.register(r'ratings', RatingViewSet, basename='ratings')
router.register(r'favorites', FavoriteViewSet, basename='favorites')

urlpatterns = [
    path('', include(router.urls)),
]
