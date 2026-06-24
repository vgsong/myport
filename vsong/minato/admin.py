from django.contrib import admin
from .models import BlogEntry, User, BlogCategory, JobTrackerEntry, CompanyName

# Register your models here.
admin.site.register(BlogEntry)
admin.site.register(BlogCategory)
admin.site.register(JobTrackerEntry)
admin.site.register(CompanyName)

