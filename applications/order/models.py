from django.db import models
from applications.product.models import Product
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self) -> str:
        return f'Название товара {self.product.name}, покупатель {self.user.email} , количество покупок - {self.quantity}, общая цена{self.total_price}, дата заказа {self.created_at} ' 

   
