# compressor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('compress/', views.compress_pdf, name='compress_pdf'),
]
