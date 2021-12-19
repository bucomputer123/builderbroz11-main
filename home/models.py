from django.db import models

# Create your models here.
class suppotors(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField(max_length=40)