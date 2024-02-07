
from django.urls import path
# from.views import result
from.views import home
from .views import spam_detector
from.views import PreditValue





urlpatterns = [
    path('check/', spam_detector, name='value'),
]
