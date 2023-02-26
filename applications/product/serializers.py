from rest_framework import serializers
from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__' # ('title',)


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Comment
        fields = '__all__'
