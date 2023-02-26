from django.db import models
from django.db import models
from applications.product.models import Product
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator , MaxValueValidator
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError

User = get_user_model()

# class Like(models.Model):
#     owner = models.ForeignKey(
#         User, on_delete=models.CASCADE,
#         related_name='likes'
#     )
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE,
#         related_name='likes'
#     )
#     is_like = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return f'{self.owner} liked - {self.product.name}'
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

    def toggle_like(self):
        self.is_like = not self.is_like
        self.save()

    
        

# class Rating(models.Model):
#     owner = models.ForeignKey(
#         User, on_delete=models.CASCADE,
#         related_name='ratings'
#     ) 
#     product =  models.ForeignKey(
#         Product, on_delete=models.CASCADE,
#         related_name='ratings'
#     )
#     rating = models.SmallIntegerField(
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(5),
#         ], blank=True,null=True
#     )

#     def __str__(self) -> str:
#         return f'{self.owner} rated {self.rating} stars for {self.product.name}'

# class Favorite(models.Model):
#     product =  models.ForeignKey(
#         Product, on_delete=models.CASCADE,
#         related_name='favorites'
#     )
#     owner = models.ForeignKey(
#         User, on_delete=models.CASCADE,
#         related_name='favorites'
#     ) 
#     favorite = models.BooleanField(default=False, blank=True, null=True)

#     def __str__(self) -> str:
#         return f'{self.owner} added {self.product.name} to favorites'

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

    def toggle_favorite(self):
            self.favorite = not self.favorite
            self.save()
            
    def __str__(self) -> str:
        return f'{self.owner} added {self.product.name} to favorites'

    


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

    def set_rating(self, value):
        if self.rating is None:
            self.rating = value
        else:
            self.rating = value
        try:
            self.clean_fields()
            self.save()
        except ValidationError as e:
            # Handle validation error
            pass
    def __str__(self) -> str:
            return f'{self.owner} rated {self.rating} stars for {self.product.name}'