from django.urls import path
from .views import WeatherList, WeatherDetail

urlpatterns = [
    path("", WeatherList.as_view(), name="weather_list"),
    path("<int:pk>/", WeatherDetail.as_view(), name="weather_detail"),
]
