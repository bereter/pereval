# Generated by Django 5.0.2 on 2024-03-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='data',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
