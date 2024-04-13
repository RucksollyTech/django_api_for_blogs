from django.contrib import admin
from .models import Profile, Blogs,Blogsz


# Register your models here.

admin.site.register(Blogs)
admin.site.register(Blogsz)
admin.site.register(Profile)

