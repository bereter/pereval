from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer


class PerevalAddedAPIView(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer