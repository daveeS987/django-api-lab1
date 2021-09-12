from rest_framework import generics
from .serializers import WeatherBlogSerializer
from .models import Weather_Blog


class WeatherList(generics.ListCreateAPIView):
    queryset = Weather_Blog.objects.all()
    serializer_class = WeatherBlogSerializer


class WeatherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weather_Blog.objects.all()
    serializer_class = WeatherBlogSerializer
