from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donasi(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description =  models.TextField()