from django.urls import path , include
from rest_framework import routers

from .views import LikeViewSet, RatingViewSet, FavoriteViewSet

router = routers.DefaultRouter()
router.register(r'likes', LikeViewSet, basename='likes') # http://localhost:8000/api/v1/feedback/likes/4/
router.register(r'ratings', RatingViewSet, basename='ratings') # http://localhost:8000/api/v1/feedback/ratings/2/
router.register(r'favorites', FavoriteViewSet, basename='favorites') #http://localhost:8000/api/v1/feedback/favorites/2/

urlpatterns = [
    path('', include(router.urls)),
]
