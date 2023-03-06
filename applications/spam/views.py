from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated

class ContactAPIView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated,]



    def perform_create(self, serializer):
        serializer.save(email=self.request.user.email)