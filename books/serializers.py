from rest_framework import serializers
from .models import Book,Favourites,Genre,Author, Review
from authorization.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=['genre_name',]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['author_name',]

class BookListSerializer(serializers.ModelSerializer):
    genre_name=GenreSerializer(source='genre')
    author_name=AuthorSerializer(source='author')

    class Meta:
        model=Book
        exclude=['genre','author','date_published','description']

class ReviewSerializer(serializers.ModelSerializer):
    user_info=UserSerializer(source='user')
    class Meta:
        model=Review
        exclude=['book','user']

class BookSelfSerializer(serializers.ModelSerializer):
    genre_name=GenreSerializer(source='genre')
    author_name=AuthorSerializer(source='author')
    reviews_list=ReviewSerializer(source='reviews')

    class Meta:
        model=Book
        exclude=['genre','author',]


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favourites
        fields='__all__'
