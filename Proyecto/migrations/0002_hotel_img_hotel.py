# Generated by Django 2.2 on 2020-11-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='img_hotel',
            field=models.ImageField(blank=True, upload_to='img_hoteles/'),
        ),
    ]
