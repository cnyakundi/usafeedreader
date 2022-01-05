# podcasts/admin.py

from django.contrib import admin

from .models import Post


@admin.register(Post)
class PosteAdmin(admin.ModelAdmin):
    list_display = ("media_house_name", "title", "pub_date")
