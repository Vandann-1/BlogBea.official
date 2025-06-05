from django.db import models
from django.contrib.auth.models import User
from blogapp.models import Blog


# Create your models here.

class Room(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    participant = models.ManyToManyField(User, related_name='participant')
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to='audio/', blank=True , null=True)
