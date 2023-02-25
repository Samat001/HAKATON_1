from django.db import models
from django.db import models
from applications.product.models import Product
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator , MaxValueValidator
from rest_framework.permissions import IsAuthenticated
User = get_user_model()

class Like(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='likes'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='likes'
    )
    is_like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.owner} liked - {self.product.name}'

class Rating(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='ratings'
    ) 
    product =  models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ], blank=True,null=True
    )

    def __str__(self) -> str:
        return f'{self.owner} rated {self.rating} stars for {self.product.name}'

class Favorite(models.Model):
    product =  models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='favorites'
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='favorites'
    ) 
    favorite = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.owner} added {self.product.name} to favorites'
