from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    phone = models
    name = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class PerevalAdded(models.Model):
    new = 'NEW'
    pending = 'PEN'
    accepted = 'ACC'
    rejected = 'REJ'

    STATUS = [
        (new, 'Новое'),
        (pending, 'В работе'),
        (accepted, 'Успешно'),
        (rejected, 'Не принято'),
    ]

    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS)
    beauntyTitle = models.TextField()
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coord_id = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level_winter = models.CharField(max_length=255)
    level_summer = models.CharField(max_length=255)
    level_autumn = models.CharField(max_length=255)
    level_spring = models.CharField(max_length=255)


class PerevalImages(models.Model):
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images')
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)


class PerevalAreas(models.Model):
    id_parent = models.IntegerField()
    title = models.TextField()


class SprActivitiesTypes(models.Model):
    titles = models.CharField()




