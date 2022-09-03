from django.contrib import admin

from .models import Book, Reference

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("isbn","search_completed")