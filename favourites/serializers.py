# favourites/serializers.py
from rest_framework import serializers
from .models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ['id', 'user', 'post', 'created_at']
