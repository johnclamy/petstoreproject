from django.contrib import admin
from .models import Pet, Review


class PetAdmin(admin.ModelAdmin):
    ordering = ['breed']
    search_fields = ['breed', 'name']


admin.site.register(Pet, PetAdmin)
admin.site.register(Review)
