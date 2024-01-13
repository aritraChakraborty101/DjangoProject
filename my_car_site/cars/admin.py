from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    fields = ['brand', 'year']
    list_display = ['brand', 'year']
    list_filter = ['brand']
    search_fields = ['brand']


admin.site.register(Car, CarAdmin)

