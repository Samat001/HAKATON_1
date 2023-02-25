from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.EmailField(required=False)
    # likes = LikeSerializer(many=True, read_only=True)
    # images = PostImageSerializer(many=True, read_only=True)
    # owner = serializers.ReadOnlyField(source='owner.email')
    
    # likes_count = serializers.SerializerMethodField()
    # def get_likes_count(self, post):
    #     return Like.objects.filter(post_id=post).count()

    class Meta:
        model = Product 
        fields = '__all__' # ('title',)


    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['like_count'] = instance.likes.filter(is_like=True).count()
    #     # rating_result = 0
    #     # for rating in instance.ratings.all():
    #     #     rating_result += rating.rating
    #     # if rating_result:
    #     #     representation['rating'] = rating_result / instance.ratings.all().count()
    #     # else:
    #     #     representation['rating'] = rating_result    
    #     representation['rating']= instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
    #     return representation
