from django.contrib import admin
from .models import Profile, Blogs


# Register your models here.

admin.site.register(Blogs)
admin.site.register(Profile)

