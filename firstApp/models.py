from django.db import models

# Create your models here.
class AndroidApp(models.Model):
    icon = models.FileField()
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    points = models.IntegerField()
