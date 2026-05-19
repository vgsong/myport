from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class BlogEntry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    category = models.ManyToManyField(BlogCategory)
    
    def __str__(self):
        return '{}: {} - {}'.format(self.created_on, self.last_modified, self.title)