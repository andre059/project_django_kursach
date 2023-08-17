from django.contrib import admin

from car.models import Owner, Car, CarHistory


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner', 'image')
    list_filter = ('year', 'owner',)


@admin.register(CarHistory)
class CarHistoryAdmin(admin.ModelAdmin):
    list_display = ('car', 'start_year', 'stop_year', 'owner')
    list_filter = ('car', 'owner',)
