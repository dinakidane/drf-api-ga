from rest_framework import viewsets
from .models import Favourite
from .serializers import FavouriteSerializer

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

