from django.contrib import admin

from Blog.models import BlogModel

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'date')


admin.site.register(BlogModel, BlogAdmin)