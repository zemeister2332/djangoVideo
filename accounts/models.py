from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class Router(models.Model):
    specifications = models.FileField(upload_to='router_specifications/%y')
    def __str__(self):
        return str(self.specifications)

class FileRouter(models.Model):
    specifications = models.FileField(upload_to='router_specifications/%y')
    title = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return str(self.title)
