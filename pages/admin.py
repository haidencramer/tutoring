from django.contrib import admin

from .models import Post

class TaAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
        
    )

admin.site.register(Post, TaAdmin)