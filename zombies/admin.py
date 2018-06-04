from django.contrib import admin

from zombies.models import MapFact, GobbleGum, Map, Perk, RandomFact


class FactInline(admin.TabularInline):
    model = MapFact


class PerkInline(admin.StackedInline):
    model = Perk
    extra = 1
    list_display = ['map', 'description']


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    model = Perk
    list_display = ['id', 'map', 'name', 'location']
    list_filter = ['map', 'name']
    list_per_page = 15


class MapFactInline(admin.TabularInline):
    model = MapFact


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    model = Map
    list_display = ['id', 'name', 'release_date']
    inlines = [PerkInline, MapFactInline]
    list_per_page = 15


@admin.register(GobbleGum)
class GobbleGumAdmin(admin.ModelAdmin):
    model = GobbleGum
    list_display = ['id', 'name', 'type']
    list_per_page = 15


@admin.register(RandomFact)
class RandomFactAdmin(admin.ModelAdmin):
    model = RandomFact
    list_display = ['description']
    list_per_page = 15

