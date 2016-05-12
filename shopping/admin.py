from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ["edit_time"]
    list_per_page = 20
    search_fields = ["name"]

admin.site.register(Category)
admin.site.register(Brands)
