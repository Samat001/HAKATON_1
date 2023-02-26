from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet ,OrderHistoryView




router = DefaultRouter()
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)), # http://localhost:8000/api/v1/order/orders/11/ крад на заказы 
    path('order_history/', OrderHistoryView.as_view(), name='order_history'),  
    
]

# http://localhost:8000/api/v1/order/order_history/ каждый пользователь может увидеть свою историю заказов для этого он должен быть авторизованным