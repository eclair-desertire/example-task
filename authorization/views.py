from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet,mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import TokenObtainPairSerializer,TokenRefreshSerializer,  UserSerializer

class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenObtainPairSerializer

class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenRefreshSerializer

class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes=[AllowAny]
    serializer_class=UserSerializer

    
# Create your views here.
