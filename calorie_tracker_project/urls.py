# calorie_tracker_project/urls.py
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('calorie_tracker.urls')),
]