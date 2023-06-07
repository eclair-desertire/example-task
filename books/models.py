from typing import Iterable, Optional
from django.db import models
from authorization.models import User


class Genre(models.Model):
    genre_name=models.CharField(verbose_name='Название жанра',max_length=255)

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'

    def __str__(self) -> str:
        return self.genre_name


class Author(models.Model):
    author_name=models.CharField(verbose_name='Имя автора',max_length=255,null=True,blank=True)

    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'

    def __str__(self) -> str:
        return self.author_name
    
class Book(models.Model):
    name=models.CharField(verbose_name='Название книги',max_length=255)
    genre=models.ForeignKey(Genre,verbose_name='Жанр',null=True,blank=True, on_delete=models.CASCADE)
    author=models.ForeignKey(Author,null=True,blank=True,on_delete=models.CASCADE)
    avg_rating=models.IntegerField(verbose_name='Средний рейтинг',default=0)
    date_published=models.DateField(verbose_name='Дата публикации',auto_now=True)

    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'

    def __str__(self) -> str:
        return self.name
    
class Review(models.Model):
    book=models.ForeignKey(Book,verbose_name='Книга',on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,verbose_name='Пользователь', on_delete=models.CASCADE)
    rate=models.IntegerField(verbose_name='Оценка',default=0)
    review_text=models.TextField(verbose_name='Текст отзыва',null=True,blank=True)

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'

    def __str__(self) -> str:
        return "Отзыв к книге: "+str(self.book)+", #"+str(self.pk)
    
    def save(self,*args,**kwargs) -> None:
        super(Review,self).save(*args,**kwargs)
        self.book.avg_rating=0
        for i in self.book.reviews.all():
            self.book.avg_rating+=i.rate
        self.book.avg_rating/=len(self.book.reviews.all())
        self.book.save()

class Favourites(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    favourite_books=models.ManyToManyField(Book,blank=True) # TODO Книги

    class Meta:
        verbose_name='Избранное'
        verbose_name_plural='Избранные'

    def __str__(self) -> str:
        return "Избранные пользователя: "+str(self.user)
        

# Create your models here.
