from django.db import models

# Create your models here.
class Trans(models.Model):
    chinese=models.CharField(max_length=100)
    english=models.CharField(max_length=200)
    test_time=models.IntegerField(default=0)
    error_time=models.IntegerField(default=0)