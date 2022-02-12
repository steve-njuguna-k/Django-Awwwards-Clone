from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_confirmed', 'date_created', 'date_updated')
    search_fields = []
    readonly_fields=('date_created', 'date_updated')
    
admin.site.register(Profile, ProfileAdmin)