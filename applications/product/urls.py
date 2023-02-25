from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet 

router = DefaultRouter()
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),# http://localhost:8000/api/v1/product/4/ детальный осмотр       общий запрос на продукты  http://localhost:8000/api/v1/product

]
