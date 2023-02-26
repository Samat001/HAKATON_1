from rest_framework import viewsets
from .serializers import ProductSerializer , CommentSerializer
from .models import Product , Comment
from .permissions import IsSuperuserOrReadOnly, IsSuperuser
import django_filters.rest_framework
from .filters import ProductFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name']
    pagination_class = ProductPagination
    permission_classes = [IsSuperuserOrReadOnly]

    @action(detail=False, permission_classes=[IsSuperuser])
    def admin_only_action(self, request, *args, **kwargs):
        # do something only superuser can do
        return Response({'message': 'This action is allowed only for superusers'})


class CommentModelViewset(ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



    