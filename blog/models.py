# blog/models.py
from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Add this field
    image = CloudinaryField('image', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)