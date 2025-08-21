from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    ordering = ['breed']


admin.site.register(Pet, PetAdmin)
