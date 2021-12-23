from django.db import models

# Create your models here.
class suppotors(models.Model):
    name = models.CharField(max_length=30,unique=True)
    amount = models.FloatField(max_length=40)
    class Meta:
        unique_together = ("name", "amount")