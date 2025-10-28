from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_at', 'is_active')
    list_filter = ('is_active','posted_at','company')
    search_fields = ('title','company','location','description')