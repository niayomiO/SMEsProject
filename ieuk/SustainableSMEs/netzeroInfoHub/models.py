from django.db import models

# Create your models here.
class Reason(models.Model):
    title = models.CharField(max_length=255)
    explanation = models.CharField(max_length=255)
