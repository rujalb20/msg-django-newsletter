from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(max_length=254,unique=True)
    token = models.CharField(max_length=30,unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
