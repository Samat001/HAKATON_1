from django.db import models
# from rest_framework import permissions  
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import OrderSerializer , OrderHistorySerializer
from .models import Order
from rest_framework import exceptions
from rest_framework import generics

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         if not self.request.user.is_authenticated:
#             raise exceptions.NotAuthenticated()
#         serializer.save(user=self.request.user)




class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            user = self.request.user
            serializer.save(user=user)
        except exceptions.ValidationError:
            serializer.is_valid(raise_exception=True)
            user = self.request.user
            serializer.validated_data['user'] = user
            serializer.save()


class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

