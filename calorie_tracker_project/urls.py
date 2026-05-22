# calorie_tracker_project/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('calorie_tracker.urls')),
]