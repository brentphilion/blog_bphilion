from django.db import models

# Create your models here.

class Post(models.Model):
    """
    To represent a blog post
    """
    title = models.Charfield(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  #set on create
    updated = models.DateTimeField(auto_now=True) #updates on save