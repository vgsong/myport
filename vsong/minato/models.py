from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class BlogEntry(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('final', 'FINAL'),
    )

    title = models.CharField(max_length=50)
    body = models.TextField()
    status = models.CharField(max_length=5,
                              choices=STATUS_CHOICES,
                              default='AC',)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_post')
    
    def __str__(self):
        return '{}: {} - ID:{} - {} on {}'.format(self.created_on, self.status, self.id, self.title, self.category)


class CompanyName(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class JobTrackerEntry(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'open'),
        ('APPLIED', 'applied'),
        ('REJECTED', 'rejected'),
        ('OFFER', 'offer'),
        ('INTERVIEWING', 'interviewing'),
    ]

    company = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='company_name')
    jobtitle = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    applied_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='OPEN')
        
    def __str__(self):
        return '{}: {} - {} - STATUS: {}'.format(self.applied_on, self.company, self.jobtitle, self.status)


class BookTrackerEntry(models.Model):
    STATUS_CHOICES = [
        ('WANT', 'want'),
        ('READING', 'reading'),
        ('FINISHED', 'finished'),
        ('GAVEUP', 'gaveup'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    started_on = models.DateField(auto_now_add=False, blank=True, null=True)
    ended_on = models.DateField(auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='OPEN')
        
    def __str__(self):
        return '{}: {} - {} - STATUS: {}'.format(self.started_on, self.author, self.title, self.status)