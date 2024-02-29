# Generated by Django 5.0.2 on 2024-02-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval_data', '0004_alter_perevaladded_coord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='connect',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='level_autumn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='level_spring',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='level_summer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='level_winter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
