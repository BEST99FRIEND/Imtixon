from django.contrib import admin
from main.models import Countries

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'territory', 'ticket_price', 'image')
