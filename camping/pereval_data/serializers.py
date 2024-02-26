from rest_framework import serializers
from .models import PerevalAdded


class PerevalAddedSerializer(serializers):

    class Meta:
        model = PerevalAdded
        fields = '__all__'
