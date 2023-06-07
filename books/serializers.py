from rest_framework import serializers
from .models import Book,Favourites,Genre,Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        extra_kwargs={
            'genre':{'source':'genre.genre_name'},
            'author':{'source':'author.author_name'}
        }

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favourites
        fields='__all__'
        