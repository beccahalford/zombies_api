from django.contrib import admin

from zombies.models import MapFact, GobbleGum, Map, Perk


class FactInline(admin.TabularInline):
    model = MapFact


class PerkInline(admin.StackedInline):
    model = Perk
    extra = 1
    list_display = ['map', 'description']


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    model = Perk
    list_display = ['id', 'name', 'location', 'map']
    list_filter = ['map', 'name']


class MapFactInline(admin.TabularInline):
    model = MapFact


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    model = Map
    list_display = ['id', 'name', 'release_date']
    inlines = [PerkInline, MapFactInline]


@admin.register(GobbleGum)
class GobbleGumAdmin(admin.ModelAdmin):
    model = GobbleGum
    list_display = ['id', 'name', 'type']
