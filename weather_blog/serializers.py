from rest_framework import serializers
from .models import Weather_Blog


class WeatherBlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "created_at", "update_at")
        model = Weather_Blog
