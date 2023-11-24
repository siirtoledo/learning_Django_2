from django.contrib import admin
from .models import Prime

# Register your models here.
@admin.register(Prime)
class PrimeaAdmin(admin.ModelAdmin):
    list_display=["title","description","author","created_on"]

# admin.site.register(Prime)