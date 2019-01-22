from django.contrib import admin
from .models import Care, Family_Care

admin.site.register(Family_Care)

class CareAdmin(admin.ModelAdmin):
    search_fields = ['name',]

admin.site.register(Care, CareAdmin)
