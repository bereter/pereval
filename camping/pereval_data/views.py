from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import PerevalAdded

class PerevalAddedAPIView(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer