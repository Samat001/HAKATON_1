from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet , CommentModelViewset


router = DefaultRouter()
router.register('', ProductViewSet)
router.register('comment', CommentModelViewset)


urlpatterns = [
    path('', include(router.urls)),# http://localhost:8000/api/v1/product/4/ детальный осмотр+крад    общий запрос на продукты  http://localhost:8000/api/v1/product
#  http://localhost:8000//api/v1/product/?search=Макбук322Про
# http://localhost:8000///api/v1/product/?brand=Asus
# http://localhost:8000/api/v1/product/?category=Ноутбуки

]
