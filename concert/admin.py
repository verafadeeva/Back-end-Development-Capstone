from django.contrib import admin

# Register your models here.
from .models import Concert


@admin.register(Concert)
class ConsertAdmin(admin.ModelAdmin):
    list_display = ("id", "concert_name", "duration", "city", "date")
    search_fields = ("concert_name",)