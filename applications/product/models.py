from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404 ,render

User = get_user_model()

# class Post(models.Model):
#     title = models.CharField('Название поста' , max_length=50, null=True , blank=True)
#     description = models.TextField('Описание поста')
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',verbose_name='Владелец поста')
#     created_at = models.DateTimeField(auto_now_add=True)
#     # image = models.ImageField(upload_to='images', null=True , blank=True)
#     john = models.CharField(max_length=50, null=True, blank=True)
#     def __str__(self) -> str:
#         return f'{self.title}'

#     def save(self):
        

#         return super().save()



# class PostImage(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='post_images')


#     def __str__(self) -> str:
#         return f'{self.post.title}'

# class Comment(models.Model):
#     owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')
#     post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
#     body =models.TextField()
#     created_at =  models.DateTimeField(auto_now_add=True)
#     updated_at =  models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return f'{self.owner} -> {self.post.title}'


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.CharField(max_length=100,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self) -> str:
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='product/%Y/%m/%d',blank=True)
    description = models.TextField(max_length=1000,blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')
    currency = models.CharField(max_length=10, default='USD', verbose_name='Валюта')
    avialable = models.BooleanField(default=True,verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Добавлен')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    class Meta:
        ordering =('name',)
        verbose_name = 'Товар'
        verbose_name_plural= 'Товары'
        index_together= (('id', 'slug'),)

    def __str__(self) -> str:
        return self.name

