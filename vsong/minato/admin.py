from django.contrib import admin
from .models import BlogEntry, User, BlogCategory, JobTrackerEntry, CompanyName, BookTrackerEntry

# Register your models here.
admin.site.register(BlogEntry)
admin.site.register(BlogCategory)
admin.site.register(JobTrackerEntry)
admin.site.register(CompanyName)
admin.site.register(BookTrackerEntry)

