from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    CHOICES = [
        ('Employeer', 'Employeer'),
        ('Job seeker', 'Job seeker'),
        
    ]
    radio_field = models.CharField(max_length=10, choices=CHOICES)