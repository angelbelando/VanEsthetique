from django.contrib import admin
from .models import Care, Family_Care

admin.site.register(Family_Care)

class CareAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    fields = ["name", "name_it", "family", 'price', 'display_order']

admin.site.register(Care, CareAdmin)
