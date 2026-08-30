from django.contrib import admin

from .models import User
from .models import BookTrackerEntry
from .models import JobTrackerEntry, CompanyName
from .models import BlogEntry, BlogCategory
from .models import XlBlogEntry, XlBlogCategory
from .models import GuestBookEntry


# Register your models here.
@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_filter = ('status', 'category', 'created_on') 

# @admin.register(BookTrackerEntry)
# class BookTrackerEntryAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'started_on') 

@admin.register(XlBlogEntry)
class XlBlogEntryAdmin(admin.ModelAdmin):
    list_filter = ('status', 'category', 'created_on')


admin.site.register(BlogCategory)
admin.site.register(XlBlogCategory)
admin.site.register(JobTrackerEntry)
admin.site.register(CompanyName)
admin.site.register(BookTrackerEntry)
admin.site.register(GuestBookEntry)

