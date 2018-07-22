from django.contrib import admin
from .models import Blog



class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","timestamp","updated"]
    list_display_links = ["timestamp"]
    list_filter=["updated","timestamp"]
    list_editable = ["title"]
    search_fields=["title","content"]
    class Meta:
        model = Blog

admin.site.register(Blog,BlogAdmin)
