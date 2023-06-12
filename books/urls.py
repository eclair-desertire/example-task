from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, FavouriteViewSet


router=DefaultRouter()
router.register('books',BookViewSet,basename='books')

urlpatterns = [
    path('',include(router.urls)),
    path('add_favourite',FavouriteViewSet.as_view({'post':'add'}))
]
