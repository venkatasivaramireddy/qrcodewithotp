from django.db import models

class DetailsModel(models.Model):
    username=models.CharField(max_length=15,unique=True)
    password=models.CharField(max_length=10)

