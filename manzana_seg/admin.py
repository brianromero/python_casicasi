from django.contrib import admin
from .models import Zona


# Register your models here.
# admin.site.register(Product)
@admin.register(Zona)
class AdminProduct(admin.ModelAdmin):
    list_display = ('ubigeo', 'zona', 'aeu', 'viv_aeu')
    list_filter = ('ubigeo','zona','aeu',)
