from django.db import models


class Map(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField()
    perks = models.ManyToManyField(through='app_name.PerkLocation')


class Location(models.Model):
    name = models.CharField()
    description = models.TextField()
    map = models.ForeignKey('app_name.Map')


class Perk(models.Model):
    name = models.CharField(choices=(
        ('quick_revive', 'Quick Revive'),
        ('juggernog', 'Juggernog'),
        ('speed_cola', 'Speed Cola'),
        ('double_tap', 'Double Tap')
    ))
    location = models.ForeignKey('app_name.Location')


class PerkLocation(models.Model):
    location = models.ForeignKey('app_name.Location')
    perk = models.ForeignKey('app_name.Perk')


class RandomFact(models.Model):
    description = models.TextField()


class Fact(models.Model):
    description = models.TextField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE)


class GobbleGum(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=100)
