from django.contrib import admin

from zombies.models import Map, Fact, Perk, Location, GobbleGum


class FactInline(admin.TabularInline):
    model = Fact


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    model = Map
    inlines = [FactInline]
    list_display = ['id', 'name']


@admin.register(GobbleGum)
class GobbleGumAdmin(admin.ModelAdmin):
    model = GobbleGum
    list_display = ['id', 'name', 'type']
