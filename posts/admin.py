from django.contrib import admin
from .models import Post, City
# Register your models here.
admin.site.register(Post)


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state")

admin.site.register(City, CityAdmin)