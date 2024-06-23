from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
from django.contrib import admin

class Sales(models.Model):
    PO_number = models.CharField(max_length=100)
    item_number = models.CharField(max_length=100)
    description = models.TextField()
    qnt = models.IntegerField()
    file = models.FileField(upload_to='uploads/', null=True, default=None)
    time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.PO_number} - {self.item_number}"
