from django.contrib import admin

from store.models import Book


@admin.register(Book)
class StoreAdmin(admin.ModelAdmin):
    pass
