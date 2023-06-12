from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet,mixins
from .serializers import BookListSerializer,BookSelfSerializer, FavouriteInitSerializer, FavouriteSerializer
from .models import Book, Favourites
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=BookSelfSerializer
    queryset=Book.objects.order_by('date_published')
    filter_backends = [DjangoFilterBackend]
    filterset_fields={
        'date_published':['gte','lte'],
        'author':['exact'],
        'genre':['exact']
    }


class FavouriteViewSet(GenericViewSet):
    serializer_class=FavouriteInitSerializer
    permission_classes=[IsAuthenticated]

    def add(self,request,*args,**kwargs):
        user=request.user
        fav=get_object_or_404(Favourites.objects.all(),user=user)
        book_id=request.data['book_id']
        book=get_object_or_404(Book.objects.all(),pk=book_id)
        favourites=fav.favourite_books.all()
        if book not in favourites:
            fav.favourite_books.add(book)
        fav.save()
        serializer=FavouriteSerializer(fav)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

# Create your views here.
