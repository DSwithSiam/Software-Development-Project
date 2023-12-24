from django.contrib import admin
from .models import *

# Register your models here.
class BrandModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('brand_name',)}
    list_display = ['brand_name', 'slug']

admin.site.register(BrandModel, BrandModelAdmin)
admin.site.register(CarModel)
admin.site.register(CommentModel)