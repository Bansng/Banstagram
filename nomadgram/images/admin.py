from django.contrib import admin
from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display_links = (
        'location',
    )

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
    )

    list_display = (
        'id',
        'file',
        'location',
        'caption',
        'creator',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'creator',
        'image'
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )
