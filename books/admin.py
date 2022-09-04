from django.contrib import admin

from .models import Book, OpenApiReference

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("isbn","quantity","search_completed")

@admin.register(OpenApiReference)
class OpenApiReferenceAdmin(admin.ModelAdmin):
    list_display = ("book","publisher","number_of_pages","title","publish_date")