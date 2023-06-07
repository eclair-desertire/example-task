from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet,mixins
from .serializers import BookSerializer
from .models import Book


class BookViewSet(GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=BookSerializer
    queryset=Book.objects.order_by('date_published')

# Create your views here.