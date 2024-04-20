from django.contrib import admin

from cars.models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = "{}" width = "40" />'.format(object.car_photo.url))


    thumbnail.short_description = 'Car Photo'
    list_display = ('id', 'thumbnail', 'car_title', 'color', 'model', 'year','is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title',)


admin.site.register(Car, CarAdmin)

