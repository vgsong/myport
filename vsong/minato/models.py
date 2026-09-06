from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field


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
    body = CKEditor5Field('TEXT', config_name='extends')
    status = models.CharField(max_length=5,
                              choices=STATUS_CHOICES,
                              default='AC',)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_posts')
    
    def __str__(self):
        return '{}: {} - ID:{} - {}'.format(self.category, self.status, self.id, self.title)


class XlBlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class XlBlogEntry(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('final', 'FINAL'),
    )

    title = models.CharField(max_length=50)
    body = CKEditor5Field('TEXT', config_name='extends')
    status = models.CharField(max_length=5,
                              choices=STATUS_CHOICES,
                              default='AC',)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='xlblog_posts')
    category = models.ForeignKey(XlBlogCategory, on_delete=models.CASCADE, related_name='xlblog_posts')
    
    def __str__(self):
        return '{}: {} - ID:{} - {}'.format(self.category, self.status, self.id, self.title)


#  TODO will remove eventually
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
#  ------------------------


class GuestBookEntry(models.Model):

    STATUS_CHOICES = [
        ('DRAFT', 'draft'),
        ('POSTED', 'posted'),

    ]

    name = models.CharField(max_length=20)
    email_contact = models.EmailField(max_length=254)
    website_url = models.URLField(max_length=250, blank=True, null=True)
    message = models.TextField() 
    status = models.CharField(choices=STATUS_CHOICES, default='draft')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}: {} - {} - STATUS: {}'.format(self.name, self.email_contact)


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
    iken = models.TextField()

        
    def __str__(self):
        return '{}: {} - {} - STATUS: {}'.format(self.started_on, self.id, self.title, self.status)


class SingEntry(models.Model):
    watching = models.CharField(max_length=50)
    playing = models.CharField(max_length=50)
    eating = models.CharField(max_length=50)
    listening = models.CharField(max_length=50)
    learning = models.CharField(max_length=50)
    feeling = models.CharField(max_length=50)
    status_message = models.CharField(max_length=200)
    
    created_on = models.DateField(auto_now_add=True)
