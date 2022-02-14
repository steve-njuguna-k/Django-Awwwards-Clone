from django.contrib import admin
from .models import Profile, Portfolio

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_confirmed', 'date_created', 'date_updated')
    search_fields = []
    readonly_fields=('date_created', 'date_updated')
    
admin.site.register(Profile, ProfileAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'portfolio_image', 'primary_language', 'category', 'date_created', 'date_updated')
    search_fields = []
    readonly_fields=('date_created', 'date_updated')
    
admin.site.register(Portfolio, PortfolioAdmin)