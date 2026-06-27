from django.contrib import admin

from .models import User
from .models import BookTrackerEntry
from .models import JobTrackerEntry, CompanyName
from .models import BlogEntry, BlogCategory
from .models import GuestBookEntry


# Register your models here.
admin.site.register(BlogEntry)
admin.site.register(BlogCategory)
admin.site.register(JobTrackerEntry)
admin.site.register(CompanyName)
admin.site.register(BookTrackerEntry)
admin.site.register(GuestBookEntry)

