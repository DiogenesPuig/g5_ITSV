# Generated by Django 2.2 on 2020-11-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0007_auto_20201122_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='img_hotel',
            field=models.ImageField(blank=True, default='maxresdefault.jpg', null=True, upload_to='img_hoteles/'),
        ),
    ]