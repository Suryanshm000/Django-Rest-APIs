# Generated by Django 3.1.4 on 2023-07-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_auto_20230701_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='androidapp',
            name='icon',
            field=models.FileField(upload_to='media/'),
        ),
    ]