from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    ordering = ['breed']
    search_fields = ['breed', 'name']


admin.site.register(Pet, PetAdmin)
