from django.contrib import admin
from .models import BlogEntry, User, BlogCategory

# Register your models here.
admin.site.register(BlogEntry)
admin.site.register(BlogCategory)

