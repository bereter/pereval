from rest_framework import serializers
from .models import PerevalAdded, PerevalImages, Coords


class PerevalCoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['title', 'img']


class PerevalAddedSerializer(serializers.ModelSerializer):
    images = PerevalImagesSerializer()
    coord_id = PerevalCoordsSerializer()
    class Meta:
        model = PerevalAdded

        fields = [
            'beauntyTitle', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coord_id', 'images', 'level_winter',
            'level_summer', 'level_autumn', 'level_spring',
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        coord_data = validated_data.pop('coord_id')
        pereval = PerevalAdded.objects.create(**validated_data)
        Coords.objects.create(pereval=pereval, **coord_data)
        PerevalImages.objects.create(pereval=pereval, **images_data)
        return pereval
        print(coord_data)

