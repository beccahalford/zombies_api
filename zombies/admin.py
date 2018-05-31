from django.contrib import admin

from zombies.models import Fact, GobbleGum, Location, Map, Perk


class FactInline(admin.TabularInline):
    model = Fact


class LocationInline(admin.StackedInline):
    model = Location
    extra = 1
    list_display = ['map', 'description']


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    model = Perk
    inlines = [LocationInline]
    list_display = ['id', 'name']


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    model = Map
    list_display = ['id', 'name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['id', 'map', 'perk', 'description']


# admin.site.register(Location)
#
# @admin.register(Map)
# class MapAdmin(admin.ModelAdmin):
#     model = Map
#     inlines = [FactInline]
#     list_display = ['id', 'name']
#
#
# @admin.register(PerkLocation)
# class PerkLocationAdmin(admin.ModelAdmin):
#     model = PerkLocation
#     list_display = ['map', 'perk', 'description']

@admin.register(GobbleGum)
class GobbleGumAdmin(admin.ModelAdmin):
    model = GobbleGum
    list_display = ['id', 'name', 'type']
