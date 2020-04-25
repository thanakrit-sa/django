from django.db import models

# Create your models here.

class article(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
