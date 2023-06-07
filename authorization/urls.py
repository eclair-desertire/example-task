from django.urls import path, include
from .views import TokenObtainPairView,TokenRefreshView,RegisterView

urlpatterns = [
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('register/',RegisterView.as_view({'post':'create'})),
]
